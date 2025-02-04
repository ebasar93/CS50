#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc != 2)
    {
        printf("Usage: recover file\n");
        return 1;
    }

    int i = 0;
    char filename[8];


    // create pointer to file
    FILE *inptr = fopen(argv[1],"r");

    // create an array of bytes
    BYTE buffer[512];
    FILE *outptr = NULL;
    // if remaining byte number is 512, continue
    while (fread(buffer,sizeof(BYTE)*512,1,inptr) == 1)
    {
        // check header if jpg
        if(buffer[0] == 0xff && buffer[1] == 0xd8 &&  buffer[2] == 0xff&&  (buffer[3] & 0xf0) == 0xe0 )
        {
        // if first jpg, create a ###.jpg file and write to file
            if (outptr == NULL)
            {
                 sprintf(filename,"%03i.jpg",i);
                 outptr = fopen(filename,"w");
                 fwrite(buffer,sizeof(BYTE)*512,1,outptr);

            }
            // else if it is not the first file close and open new one
            else
            {
                fclose(outptr);
                i++;
                sprintf(filename,"%03i.jpg",i);
                outptr = fopen(filename,"w");
                fwrite(buffer,sizeof(BYTE)*512,1,outptr);
            }
        }
        else if (outptr != NULL)
        {
            fwrite(buffer,sizeof(BYTE)*512,1,outptr);
        }
    }
    //return 0; olsa da olur olmasa da

}