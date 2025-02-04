#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>


bool only_digits(string text);
char rotate(char c, int i);

int main(int argc, string argv[])
{
    // if there are more than 1 argument, return 1
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;


    }
    // ! for not true
    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;

    }
    string ptext = get_string("Plaintext: ");
    printf("ciphertext: ");
    int am = atoi(argv[1]);                                 // convert argument string to integer
    for (int i = 0, n = strlen(ptext); i < n; i++)          // call rotate function to print
    {
        printf("%c", rotate(ptext[i], am));
    }
    printf("\n");
}

bool only_digits(string text)

{
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // you must turn char to int first before calling the function as it just compares the number on the ASCI maybe
        int c = text[i];
        if (!isdigit(c))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (!isalpha(c))                                    // if not alpha return as same
    {
        return c;
    }

    if (isupper(c))                                      // make A(65) equal to 0
    {
        c -= 65;
        int newc = (c + n) % 26 + 65;
        return (char) newc;
    }
    else                                                 // make a(97) equal to 0
    {
        c -= 97;
        int newc = (c + n) % 26 + 97;
        return (char) newc;
    }

}

