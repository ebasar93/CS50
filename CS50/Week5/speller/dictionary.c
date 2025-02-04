// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    /// length is defined in dictionary.h as length of the longest word
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

/// initial dictionary size loaded
int dsize = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int i = hash(word);
    /// create cursor to point at the head of the linked list
    node *cursor = table[i];
    while (cursor != NULL)
    {
        if (strcasecmp(word,cursor->word) == 0)
            {
                return true;
            }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    /// open dictionary
    FILE *file = fopen(dictionary,"r");
    if (file == NULL)
    {
        printf("Usage: dictionary is NULL\n");
        return false;
    }
    /// read string from file
    char dword[LENGTH + 1];
    ///
    //for(int am = 0;am < 2; am++)
    while (fscanf(file,"%s",dword)!= EOF)
    {
        /// create a new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
            {
                unload();
                printf("No memory\n");
                return false;
            }
        strcpy(n->word, dword);
        /// valgrind error
        n->next = NULL;
        /// keep track of words loaded from dictionaty to memory
        dsize++;
        /// find bucket number
        int i = hash(dword);
        /// assign node pointer to be same as first element pointer by the array[i]
        n->next = table[i];
        /// assign first element pointer to the new node
        table[i] = n;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    return dsize;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for(int i = 0;i < N;i ++)
    {
        node *cursor = table[i];
        node *temp = cursor;
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(temp);
            temp = cursor;

        }
        
    }
    return true;
}
