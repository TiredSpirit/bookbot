def word_count(text):
    words = text.split()
    return len(words)

def letter_count(book_text):
    lowercase_words = book_text.lower()
    char_counts = {}
    for char in lowercase_words:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def sort_characters(letter_count):
    chars_list = []
    for char, count in letter_count.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    def sort_on(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
