def main():
    filepath = "books/frankenstein.txt"
    whole_book = get_book_text(filepath)
    word_count = count_words(whole_book)
    print(word_dictionary_count(whole_book))

def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
     
def word_dictionary_count(book_string):
    letter_dict = {}
    lowercase = book_string.lower()
    for letter in lowercase:
        if letter not in letter_dict:
            letter_dict[letter] = 0
        letter_dict[letter] += 1
    return letter_dict

main()