from stats import count_words
from stats import char_occurrence
from stats import sorted_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count -----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count --------")
    char_count = char_occurrence(book_text)
    sorted_count = sorted_dictionary(char_count)
    for c in sorted_count:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['count']}")

def get_book_text(path: str):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()

