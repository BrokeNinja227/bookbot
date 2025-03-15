import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

print ("============ BOOKBOT ============")
print ("Analyzing book found at books/frankenstein.txt...")
print ("----------- Word Count ----------")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

text = get_book_text(book_path)

from stats import get_word_count
main_word_count = get_word_count(text)
print (f"Found {main_word_count} total words")

print ("--------- Character Count -------")

from stats import character_count
main_char_count = character_count(text)

from stats import dict_to_list
main_dict_to_list = dict_to_list(main_char_count)

from stats import sort_dict
sorted_list = sort_dict(main_dict_to_list)

def remove_non_alpha(sorted_list):
    filtered_list = []
    for item in sorted_list:
        if item['char'].isalpha():
            filtered_list.append(item)
    return filtered_list

filtered_list = remove_non_alpha(sorted_list)
for item in filtered_list:
    print (f"{item['char']}: {item['num']}")

print ("============= END ===============")
