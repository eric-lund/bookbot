def main():
    filepath = "books/frankenstein.txt"
    whole_book = get_book_text(filepath)
    word_count = count_words(whole_book)
    print(word_count)

def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
     
main()