def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count

from stats import letter_count

from stats import sort_characters

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = word_count(book_text)
    num_letters = letter_count(book_text)
    sorted_chars = sort_characters(num_letters)
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        character = item["char"]
        count = item["count"]
        if not character.isalpha():
            continue
        print(f"{character}: {count}")
    print("============= END ===============")
        
main()