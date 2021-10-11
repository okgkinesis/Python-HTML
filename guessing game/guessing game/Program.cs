using System;

namespace NumberGuessingGame
{
    class Program
    {
        static void Main(string[] args)

        {
            bool repeat = true;

            while (repeat != false)
            {
                bool realInteger = false;
                Random rand = new Random();
                int userNumberGuess = 0;
                int count = 0;
                string input;

                Console.WriteLine("Welcome to the number guessing game!");

                bool correctGuess = false;

                Console.Write("Please choose a number range to play in: ");
                Console.Write("start number.");
                input = Console.ReadLine();
                int userFirst = int.Parse(input);
                Console.Write("end number");
                input = Console.ReadLine();
                int userLast = int.Parse(input);

                int randomNumber = rand.Next(userFirst, userLast + 1);

                while (correctGuess != true)
                {
                    count = count + 1;


                    Console.Write("Please make a guess: ");
                    string userInput = Console.ReadLine();

                    realInteger = int.TryParse(userInput, out userNumberGuess);

                    if (realInteger == false || userNumberGuess < userFirst || userNumberGuess > userLast)
                    {
                        Console.WriteLine($"Sorry, the number needs to be a whole number between {userFirst} and {userLast}.");
                        continue;
                    }



                    if (randomNumber > userNumberGuess)
                    {
                        Console.WriteLine($"The number is more than {userNumberGuess}");

                    }
                    else if (randomNumber < userNumberGuess)
                    {
                        Console.WriteLine($"the number is less than{userNumberGuess}");

                    }
                    else
                    {
                        Console.WriteLine($"Congratulations! THe correct number is: {userNumberGuess}.");
                        correctGuess = true;

                    }
                }

                Console.WriteLine($"It took {count} Guesses. Thanks for playing!");
                Console.WriteLine("Would you like to play again?:  (Y/N)");
                string answer = Console.ReadLine();
                if (answer.ToUpper() == "N")
                {
                    repeat = false;
                }
            }
        }
    }
}
