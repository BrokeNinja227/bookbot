def get_word_count (text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_count (text):
    lower_case_text=str.lower(text)
    char_count={}
    for i in lower_case_text:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def dict_to_list(single_dict):
    unsorted_dict_list = []
    for key, value in single_dict.items():
        unsorted_dict_list.append({'char': key, 'num': value})
    return unsorted_dict_list

def sort_on(unsorted_dict_list):
    return unsorted_dict_list["num"]

def sort_dict(unsorted_dict_list):
    unsorted_dict_list.sort(reverse=True, key=sort_on)
    return(unsorted_dict_list)
