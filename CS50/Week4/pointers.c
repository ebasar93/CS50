#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(void)
{
    char *s = "HI!";
    printf("%p\n", s);  // print address of first char
    printf("%c\n", *s); // print first char dereference
    printf("%s\n", s);   // print string
    int n = 31;
    int *p = &n;        // pointer at location of integer n
    printf("%p\n", p);  // print int location
    printf("%i\n", *p); // dereference to print integer
    printf("%p\n", &n);  // print int location
    // int *p = 50; error incompatible integer to pointer conversion

    // int *am[10] = {1,3,4,6,6,76}; error incompatible integer to pointer conversion
    int am[10];
    printf("%p\n", &am);  /// print first element of location of array
    printf("%p\n", &am[0]); /// print first element of location of array
    //am[-1] ve am[11] den sonrasi calismiyor


    RGBTRIPLE(*image)[50] = calloc(50, 50 * sizeof(RGBTRIPLE));
    int *exarray = malloc (10);
    printf("%p\n", exarray);  /// print location of first element of array
    for (int i =0; i<10; i++)
    {
        printf("%i\n", exarray[i]);  /// *exarray[i] did not work error indirection requires pointer operand
    }
    printf("%i\n", *exarray); /// print first element of location of array which is 0
    int(*got)[50] = calloc(50, 50 * sizeof(int));
    got[1][1] = 90;             // assign 90 to array got
    printf("%i\n", got[1][1]);
    printf("%i\n", got[3][1]);







}
