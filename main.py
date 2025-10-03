from stats import *
import sys


# Gets the Text Content of a file and returns it.
def get_book_text(file_path=str):
    # Executes Effectively a Try-Except statement, assigning the file object to f.
    with open(file_path) as f:
        # f is treated as a file object and is read, getting the contents of the file.
        return str(f.read())

def main():
        book_path, file_content = str, str; #"books/frankenstein.txt"
        
        # Checks if any arguments are passed by the system, prompts the user for a path otherwise.
        if len(sys.argv) < 2: 
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            book_path = str(sys.argv[1])
            
        print(f"{"=" * 50}\n BOOKBOT \n{"=" * 50}\nAnalyzing book found at {book_path}...")
        file_content = get_book_text(book_path)
        
        word_count = get_word_count(file_content)
        char_dict = get_char_dict(file_content)
        
        print(f"{"="*75}\n{file_content}\n{"="*75}")
        
        print(f"\nWord Count")
        print(f"Found {word_count} total words\n{"=" * 50}")
        
        print(f"{"-" * 10} Character Count {"-" * 10}")
        for char in sort_char_dict(char_dict):
            if char["char"].isalpha(): # Checks if the String/Character contains a alphabetical character.
                print(f"{char["char"]}: {char["num"]}")
        print(f"{"-" * 50}")
                
        print(f"{"=" * 10} Found END total words {"=" * 10}")
        print(sys.argv)
        
main()