using System;
using System.Linq;

namespace ConsoleTest
{
    class Program
    {
        static void Main(string[] args)
        {
            #region input
            string[] input = {
                
            };
            #endregion input
            try
            {
                for (int i = 0; i < input[0].Length; i++)
                    Console.Write(mostCommon(input, i));

                Console.WriteLine("\n");
                for (int i = 0; i < input[0].Length; i++)
                    Console.Write(leastCommon(input, i));

            } catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }

            Console.WriteLine("\nDone.\n");
            Console.ReadKey();
        }

        static string mostCommon(string[] input, int col)
        {
            var colArr = input.Select(line => { return line.Substring(col, 1); });
            var counts = colArr.Distinct().Select<string, Tuple<string, int>>((letter) => { return new Tuple<string, int>(letter, colArr.Count((entry) => { return entry == letter; })); });
            return counts.Where((entry) => { return entry.Item2 == counts.Max(count => count.Item2); }).First().Item1;
        }

        static string leastCommon(string[] input, int col)
        {
            var colArr = input.Select(line => { return line.Substring(col, 1); });
            var counts = colArr.Distinct().Select<string, Tuple<string, int>>((letter) => { return new Tuple<string, int>(letter, colArr.Count((entry) => { return entry == letter; })); });
            return counts.Where((entry) => { return entry.Item2 == counts.Min(count => count.Item2); }).First().Item1;
        }
    }
}
