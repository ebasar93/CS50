import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print("Usage: python DNA.py FILENAME")
        sys.exit(0)

    # TODO: Read database file into a variable
    profiles = []
    headers = []
    database = sys.argv[1]
    with open(database) as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            profiles.append(row)

    # TODO: Read DNA sequence file into a variable
    sequence = ""
    database = sys.argv[2]
    with open(database) as f:
        reader = csv.reader(f)
        sequence = next(reader)[0]

    # TODO: Find longest match of each STR in DNA sequence
    strdna = headers[1:]
    results = []
    for i in strdna:
        results.append(longest_match(sequence,i))
    # TODO: Check database for matching profiles
    ans = []
    dummy = 0
    for i in profiles:
        dummy = 0
        for j in range(len(i[1:])):
            if int(i[j+1]) != results[j]:
                dummy = 1
                break
        if dummy == 0:
            ans = i
            break
    if dummy == 0:
        print(ans[0])
    else:
        print('No match')

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
