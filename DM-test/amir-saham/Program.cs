using System;
using System.Collections.Generic;

namespace amir_saham
{
    class Program
    {
        public static bool condition(int i, int j) => i != j-1;
        public static List<string> blank(int soton)
        {
            var output = new List<string>();
            for(int i=0; i<soton; i++)
            {
                if(i == 0)
                {
                    output.Add("|");
                } else {
                    output.Add(" ");
                }
            }
            return output;
        }
        public static void fill(List<List<string>> output, int satr)
        {
            for(int i=0; i<output.Count; i++)
            {
                if((i == output.Count-1) || (i == satr)) { continue;
                } else {
                    output[i].Add(" ");
                }
            }
        }
        public static List<List<string>> nemodar(string input)
        {
            var output = new List<List<string>>();
            for(int i=0; i<2; i++)
            {   output.Add(new List<string>());     }
            for(int i = 0; i<input.Length+3; i++)
            {
                if(i==0)
                    output[output.Count-1].Add("+");
                else
                    output[output.Count-1].Add("-");
            }            
            for(int i=0; i<output.Count-1; i++)
            {   output[i].Add("|"); output[i].Add(" ");    }
            char[] c_arr_input = input.ToCharArray(); int satr = output.Count-2; int soton = 2;
            for(int i=0; i<c_arr_input.Length; i++)
            {
                if(satr == -1)
                {   output.Insert(0, blank(soton)); satr++; }
                if(satr == output.Count-1)
                {   output.Insert((output.Count-1), blank(soton)); }
                if(c_arr_input[i] == 'R')
                {   output[satr].Add("/"); fill(output, satr);
                    if(condition(i, c_arr_input.Length))
                    {   satr = harkat(c_arr_input[i], c_arr_input[i+1], satr); soton++; }
                }
                else if(c_arr_input[i] == 'C')
                {   output[satr].Add("_"); fill(output, satr); 
                    if(condition(i, c_arr_input.Length))
                    {   satr = harkat(c_arr_input[i], c_arr_input[i+1], satr); soton++; }
                }
                else if(c_arr_input[i] == 'F')
                {   output[satr].Add("\\"); fill(output, satr);
                    if(condition(i, c_arr_input.Length))
                    {   satr = harkat(c_arr_input[i], c_arr_input[i+1], satr); soton++; }   
                }
            }
            return output;            
        }

        private static int harkat(char v1, char v2, int satr)
        {
            if((v1=='R' && v2=='F')||(v1=='C' && v2=='R')||(v1=='C' && v2=='C')||(v1=='F' && v2=='C')||(v1=='F' && v2=='R'))
            {    return satr;}
            else if((v1=='C' && v2=='F')||(v1=='F' && v2=='F'))
            {    return satr + 1;}
            else
            {    return satr - 1;}
        }

        static void Main(string[] args)
        {
            List<List<string>> output = nemodar(Console.ReadLine());
            for(int i=0; i<output.Count; i++)
            {
                for(int j=0; j<output[i].Count; j++)                
                    System.Console.Write(output[i][j]);
                if(i+1 != output.Count)
                    System.Console.WriteLine();
            }                
        }
    }
}
