#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Width: ");
    }
    while (n < 1 || n > 8) ;
    for(int i=0; i<n; i++)
    {
        for(int j=1; j<n-i; j++)
        {
            printf(" ");
        }

        for(int k=0; k<=i; k++)
        {
            printf("#");
        }
        printf("  ");
        for(int l=0; l<=i; l++)
        {
            printf("#");
        }
    printf("\n");
    }

}