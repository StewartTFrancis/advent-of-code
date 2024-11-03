using System.Text;

public static class Day1
{
    public static void Part1()
    {
        using FileStream fs = File.OpenRead(@"Day1.txt");
        using TextReader input = new StreamReader(fs);

        string numberLine;
        int numbers = 0;

        int total = 0;

        string line = input.ReadLine();
        while (line != null)
        {
            line = fixNums(line);
            numberLine = line.Substring(0, 1) +  line.Substring(line.Length - 1, 1);

            if (int.TryParse(numberLine, out numbers))
                total += numbers;

            line = input.ReadLine();
        }

        Console.WriteLine(total);
    }

    private static string fixNums(string input)
    {
        StringBuilder line = new StringBuilder();

        var numChars = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        var numWords = new string[] { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

        // We need to walk front to back as some of the input has overlapping numbers as their text equivalent, ex: twone... which should resolve as 21 as far as we're concerned.
        for(var i = 0; i < input.Length; i++)
        {
            // If it's a number, plop it on the stack, otherwise we don't need it anyway.
            if(numChars.Contains(input[i]))
                line.Append(input[i]);
            else
            {
                // I'm sure there's a better way to walk though these w/ lambdas... but eh
                for (int j = 0; j < numWords.Length; j++)
                {
                    if (numWords[j].Length + i <= input.Length && input.Substring(i, numWords[j].Length) == numWords[j])
                        line.Append(j.ToString());
                }
            }
        }
        

        return line.ToString();
    }
}