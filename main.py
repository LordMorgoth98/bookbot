def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = get_character_count(text)
    character_count_list = [{"name": char, "num": count} for char, count in character_counts.items()]
    character_count_list.sort(reverse=True, key=dict_sort_on_num)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in character_count_list:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    text = text.lower()
    character_count = {}
    for char in text:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def dict_sort_on_num(dict):
    return dict["num"]


main()
