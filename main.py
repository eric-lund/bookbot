def main():
    filepath = "books/frankenstein.txt"
    whole_book = get_book_text(filepath)
    list_of_letters = word_dictionary_count(whole_book)
    print_output(list_of_letters)


def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
     
def word_dictionary_count(book_string):
    letters = []
    letter_dict = {}
    # change all characters to lowercase
    lowercase = book_string.lower()
    
    for letter in lowercase:
        # we only want alpha characters
        if letter.isalpha():
            # if the letter doesn't exist yet
            # # we have to set to 0 first
            if letter not in letter_dict:
                letter_dict[letter] = 0
            letter_dict[letter] += 1

    # Creates a new dictionary with named
    # columns or whatever they are
    for charcter, count in letter_dict.items():
            new_dict = {"char": charcter, "count": count}
            letters.append(new_dict)

    letters.sort(reverse=True, key=sort_on_key)
    return letters

def sort_on_key(dict):
    return dict["count"]

def print_output(book):  
    for char in book:
        print(f"The '{char["char"]}' character was found {char["count"]} times.")

main()