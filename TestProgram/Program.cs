using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace TestProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            int start = Convert.ToInt32(args[0]);
            int end = Convert.ToInt32(args[1]);
            for (int i = start; i < end; i++)
            {
                if (i % 2 == 1)
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
