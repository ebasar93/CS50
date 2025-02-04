from cs50 import get_string

def main():
    Text = get_string("Text: ")
    l = count_letters(Text);
    w = count_words(Text);
    s = count_sentences(Text);
    i = calc_index(l, w, s);
    if i < 1:
        print("Before Grade 1")
    elif i >= 1 and i <= 15:
        print(f"Grade {i}")
    else:
        print("Grade 16+")


def count_letters(Text):
    am = 0
    for c in Text:
        if c.isalpha():
            am += 1

    return am


def count_words(Text):
    am = 1
    for c in Text:
        if c == " ":
            am += 1
    return am


def count_sentences(Text):
    am = 0
    for i in Text:
        if i in ['!', '.','?']:
            am += 1
    return am


def calc_index(l,w,s):
    i = 0.0588 * l * 100 / w - 0.296 * s * 100 / w - 15.8
    return round(i)


main()

