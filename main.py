import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
from stats import get_word_count

from stats import char_count               # Imports functions written in stats.py to be used in main.py

from stats import sorted_list
    
def main():
    # Variable, easy to change if we need to read a diff book.
    # Calls the first function, reads the path/book, and prints the results here.
    book_txt = get_book_text(path)
    # Calls word count, and uses book_txt from the first function as a variable.
    word_count = get_word_count(book_txt)
    # Calls char count, and lists the count of each character from the book_txt var.
    chars = char_count(book_txt)
    # Prints each character and its occurence in a sorted list.
    sorted_chars = sorted_list(chars)
    
    # Report Format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Char count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")


    print("============= END ===============")


main()


