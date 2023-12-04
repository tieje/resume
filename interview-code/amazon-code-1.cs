using System;

class Program
{
    static void Main()
    {
        int number = int.Parse(Console.ReadLine());

        if (number >= 0)
        {
            long result = Factorial(number);
            Console.WriteLine($"{result}");
        }
        else
        {
            Console.WriteLine("The number must be non-negative");
        }
    }

    static long Factorial(int n)
    {
        if (n == 0 || n == 1)
        {
            return 1;
        }
        else
        {
            return n * Factorial(n - 1);
        }
    }
}
