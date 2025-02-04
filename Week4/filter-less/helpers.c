#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int am =  round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtBlue = am;
            image[i][j].rgbtGreen = am;
            image[i][j].rgbtRed = am;

        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);

            image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
            image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
         }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    // copy image to temp

    for (int i = 0; i < height; i++)
    {
        if (width % 2 == 0)
        {
            for (int j = 0; j < width / 2; j++)
            {
                RGBTRIPLE temp[height][width];
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp[i][j];
            }
        }

        else if (width % 2 != 0)
        {
            for (int j = 0; j < (width - 1) / 2; j++)
            {
                RGBTRIPLE temp[height][width];
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp[i][j];
            }
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // create and allocate memory

    RGBTRIPLE(*temp)[width * 2] = calloc(height * 2, (width * 2) * sizeof(RGBTRIPLE));

    // create temp -1 all-around

    for (int i = 0; i < height + 2; i++)
    {
        for (int j = 0; j < width + 2; j++)
        {

             temp[i][j].rgbtBlue = 'a';
             temp[i][j].rgbtGreen = 'a';
             temp[i][j].rgbtRed = 'a';
        }
    }

    /// copy image to temp
    for (int i = 1; i < height +1 ; i++)
    {
        for (int j = 1; j < width +1; j++)
        {
             temp[i][j].rgbtBlue = image[i-1][j-1].rgbtBlue;
             temp[i][j].rgbtGreen = image[i-1][j-1].rgbtGreen;
             temp[i][j].rgbtRed = image[i-1][j-1].rgbtRed;
        }
    }

    for (int i = 1; i < height +1; i++)
    {
        for (int j = 1; j < width +1; j++)
        {
            int n = 0;
            int sumred = 0;
            int sumblue = 0;
            int sumgreen = 0;
            for (int k = -1 ; k < 2 ; k++)
            {
                for (int l = -1 ; l < 2; l++)
                {
                    if (temp[i + k][j + l].rgbtBlue == 'a' && temp[i + k][j + l].rgbtRed == 'a' && temp[i + k][j + l].rgbtGreen == 'a' )
                    {
                        continue;
                    }
                    else
                    {
                        sumred += temp[i + k][j+l].rgbtRed;
                        sumblue += temp[i + k][j + l].rgbtBlue;
                        sumgreen += temp[i + k][j + l].rgbtGreen;
                        n += 1;
                    }
                }
            }

           image[i-1][j-1].rgbtBlue = round(sumblue / n);
           image[i-1][j-1].rgbtGreen = round(sumgreen / n);
           image[i-1][j-1].rgbtRed = round(sumred / n);
        }
    }
    free(temp);
    return;
}
