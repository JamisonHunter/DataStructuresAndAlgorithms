// This code guesses values between 1 and 10 until it gets the correct answer.

sbyte number = 3;

Random value = new Random();

do{
    sbyte guess = (sbyte)value.Next(1, 11);
    Console.WriteLine($"Computer guesses: {guess}");
    if(guess == number){
        Console.WriteLine($"The computer guessed {number} correctly!");
        break;

    }
} while(true);