#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string word);
int count_words(string word);
int count_sentences(string Text);
int calc_index(int l, int w, int s);
void print(int i);

int main(void)
{
    string Text = get_string("Text: ");
    int l = count_letters(Text);
    int w = count_words(Text);
    int s = count_sentences(Text);
    int i = calc_index(l, w, s);
    print(i);

}

int count_letters(string Text)
{
    int am = 0 ;
    for (int i = 0, n = strlen(Text); i < n; i++)
    {
        // if char is alphabetic, increase am
        if isalpha(Text[i])
        {
            am++;
        }
    }
    return am;
}

int count_words(string Text)
{
// start am by 1 as last word of text is not included otherwis
    int am = 1 ;
    for (int i = 0, n = strlen(Text); i < n; i++)
    {
        // convert char to integer , maybe a shorter way can be found
        int a = Text[i];
        // if char is space increase am
        if (a == 32)
        {
            am++;
        }
    }
    return am;
}

int count_sentences(string Text)
{
    int am = 0 ;
    for (int i = 0, n = strlen(Text); i < n; i++)
    {
        int a = Text[i];
        // if char is '!', '.' or '?', add 1 to am
        if (a == 33 || a == 46 || a == 63)
        {
            am++;
        }
    }
    return am;
}

int calc_index(int l,int w, int s)
// calculates index
{
    float i = 0.0588 * l * 100 / w - 0.296 * s * 100 / w - 15.8;
    int rounded = round(i);
    return rounded;
}

void print(int i)
//prints Grade Level
{
    if (i < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (i >= 1 && i <= 15)
    {
        printf("Grade %i\n", i);
    }
    else
    {
        printf("Grade 16+\n");
    }
}


