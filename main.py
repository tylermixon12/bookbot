from stats import get_word_count
from stats import get_char_dict
from stats import sort_char_dict
import sys


def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {get_word_count(file_path)} total words")
        print("--------- Character Count -------")
        for char_dict in sort_char_dict(get_char_dict(file_path)):
            if (char_dict['char'].isalpha()):
                print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")
main()