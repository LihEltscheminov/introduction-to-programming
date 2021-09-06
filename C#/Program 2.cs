using System;

namespace P1_Vecka2_GenomGang
{
    class Program
    {
        static void Main(string[] args)
        {
            string namn, input;
            int alder;
            float langd, vikt;
            

            Console.WriteLine("Hej! Vad heter du?");
            namn = Console.ReadLine();
            Console.WriteLine("Hejsan " + namn + "!");

            Console.WriteLine("Hur gammal är du?");
            input = Console.ReadLine();
            Int32.TryParse(input, out alder);
            Console.WriteLine("Ok, din ålder är " + alder + ".");

            Console.WriteLine("Hur lång är du i cm?");
            langd = float.Parse(Console.ReadLine());
            Console.WriteLine("Ok, din langd är " + langd + "cm.");
            float langdMeter = langd / 100;

            Console.WriteLine("Hur mycket väger du i kg?");
            vikt = float.Parse(Console.ReadLine());
            Console.WriteLine("Ok, du väger " + vikt + "kg.");

            float bmi = vikt / (langdMeter * langdMeter);
            Console.WriteLine(namn + ", du är " + alder + "år, " + langdMeter + "m lång och väger " + vikt + "kg. Din beräknade BMI är " + Math.Round(bmi,1)+ ".");

            }
    }
}
