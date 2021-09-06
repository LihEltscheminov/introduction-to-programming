using System;

    namespace UPG3_Program1
    {
        class Program
        {
            static bool programQuit = false;

        static void Main(string[] args)
            {
                while (programQuit == false)
                {
                MainMenuText();
                }
            static void MainMenuText()
            {
                Console.WriteLine("Hej, Gör ditt val:");
                Console.WriteLine("1: Skriv ut 1 till 100.");
                Console.WriteLine("2: Skriv ut 100 till 1.");
                Console.WriteLine("3: Avsluta program");
                string userChoice = Console.ReadLine();
            
                if (userChoice == "1")
                {
                    Console.WriteLine("Du har gjort val 1");
                    Counter(true);
                    KeepTrying();
                }
                else if (userChoice == "2")
                {
                    Console.WriteLine("Du har gjort val 2");
                    Counter(false);
                    KeepTrying();
                }
                else if (userChoice == "3")
                {
                    Console.WriteLine("Programmet avslutas");
                    programQuit = true;
                }
                else
                {
                    if (true)
                    {
                    Console.WriteLine("Ditt val är ej giltigt, prova igen.");
                    MainMenuText();
                    }
                }
            }

            static void KeepTrying()
            {
                Console.WriteLine("vill du försöka igen ?");
                Console.WriteLine("*: För ja.");
                Console.WriteLine("#: För nej.");
                string userChoiceAgain = Console.ReadLine();

                if (userChoiceAgain == "*")
                {
                    Console.WriteLine("Du kommer att spela igen.");
                    MainMenuText();
                }
                else if (userChoiceAgain == "#")
                {
                    Console.WriteLine("Programmet avslutas");
                    programQuit = true;
                }
                else
                {
                    Console.WriteLine("Ditt val är ej giltigt, prova igen.");
                    KeepTrying();
                }

            }


            static void Counter (bool countUp)
            {
                    if(countUp==true)
                    {
                        for(int i=0; i<100; i++)
                        {
                            Console.WriteLine(i + 1);
                        }
                    }
                    else
                    {
                        for(int i=100; i>0; i--)
                        {
                            Console.WriteLine(i);
                        }
                    }
            }
            }
        }
    }



