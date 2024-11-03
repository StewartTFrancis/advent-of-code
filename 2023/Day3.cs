

public static class Day3
{
    public static void Part1()
    {
        using FileStream fs = File.OpenRead(@"Day3.txt");
        using TextReader input = new StreamReader(fs);

        string line = input.ReadLine();
        while (line != null)
        {
        }
    }

    private static char[][] parseGrid(TextReader input)
    {
        // I realize that this is kind of cheeky... but none of this is ever going to be production code.
        List<char[]> grid = new List<char[]>();

        string line = input.ReadLine();
        while (line != null)
        {
            grid.Add(line.ToCharArray());
        }
        
        return grid.ToArray();
    }

    public static void Part2()
    {
        using FileStream fs = File.OpenRead(@"Day3.txt");
        using TextReader input = new StreamReader(fs);

        
    }
}