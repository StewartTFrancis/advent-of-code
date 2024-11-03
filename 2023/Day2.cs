
public static class Day2
{
    public static void Part1()
    {
        Dictionary<string, int> maxValid = new Dictionary<string, int>() 
        { 
            {"red", 12},
            {"green", 13},
            {"blue", 14}
        };

        using FileStream fs = File.OpenRead(@"Day2.txt");
        using TextReader input = new StreamReader(fs);

        Dictionary<string, int> found = new Dictionary<string, int>()
        {
            {"red", 0},
            {"green", 0},
            {"blue", 0}
        };

        int game = 0;
        int sum = 0;

        // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        string line = input.ReadLine();
        bool allPossible = true;
        while (line != null)
        {
            allPossible = true;
            // There's a bunch of things I feel like are going to change in part 2.
            // But... we'll cross that bridge in part 2.

            // Also, this makes some pretty unsafe assumptions about the string.
            var gameCountSplit = line.Split(":");

            // This in particular is liable to blow up.
            game = int.Parse(gameCountSplit[0].Substring(5));

            // Each "grab", delimited by a semi-colon is treated separately
            var grabs = gameCountSplit[1].Split([';']);

            foreach(var grab in grabs)
            {
                found["red"] = 0;
                found["green"] = 0;
                found["blue"] = 0;
                
                var ColorCounts = grab.Trim().Split(",");

                foreach(var colorCount in ColorCounts)
                {
                    var split = colorCount.Trim().Split(" ");
                    found[split[1]] += int.Parse(split[0]);
                }

                if(!foundPossible(maxValid, found))
                {
                    allPossible = false;
                    continue;
                }
            }

            if(allPossible)
                sum += game;

            line = input.ReadLine();
        }

        Console.WriteLine(sum);
    }

    private static bool foundPossible(Dictionary<string, int> max, Dictionary<string, int> found)
    {
        foreach(var key in found.Keys)
        {
            if(!max.ContainsKey(key) || max[key] < found[key])
                return false;
        }

        return true;
    }

    public static void Part2()
    {
        using FileStream fs = File.OpenRead(@"Day2.txt");
        using TextReader input = new StreamReader(fs);

        Dictionary<string, int> minPossible = new Dictionary<string, int>() 
        { 
            {"red", 0},
            {"green", 0},
            {"blue", 0}
        };

        Dictionary<string, int> found = new Dictionary<string, int>()
        {
            {"red", 0},
            {"green", 0},
            {"blue", 0}
        };

        int sum = 0;

        // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        string line = input.ReadLine();
        bool allPossible = true;
        while (line != null)
        {
            var gameCountSplit = line.Split(":");

            // Each "grab", delimited by a semi-colon is treated separately
            var grabs = gameCountSplit[1].Split([';']);

            // Reset minPossible every game
            minPossible["red"] = 0;
            minPossible["green"] = 0;
            minPossible["blue"] = 0;


            foreach(var grab in grabs)
            {
                // Reset found every grab
                found["red"] = 0;
                found["green"] = 0;
                found["blue"] = 0;
                
                var ColorCounts = grab.Trim().Split(",");

                foreach(var colorCount in ColorCounts)
                {
                    var split = colorCount.Trim().Split(" ");
                    found[split[1]] += int.Parse(split[0]);
                }

                // Go through the found for this grab, and ensure minPossible is high enough to cover it.
                foreach (var key in found.Keys)
                {
                    if (minPossible[key] < found[key])
                        minPossible[key] = found[key];
                }
            }

            // Add the power to the sum
            sum += minPossible["red"] * minPossible["green"] * minPossible["blue"];
            
            line = input.ReadLine();
        }

        Console.WriteLine(sum);
    }
}