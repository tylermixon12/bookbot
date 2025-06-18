def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
        
def get_word_count (file_path):
    file_contents = get_book_text(file_path)
    words = file_contents.split()
    count = 0
    for i in words:
        count += 1
    return count

def sort_on(dict):
    return dict["num"]

def get_char_dict(file_path):
    char_dict = {}
    #Converto to lowercase
    file_contents = get_book_text(file_path).lower()

    #Count instances of each character and add to dict
    for i in file_contents:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
        
    return char_dict

def sort_char_dict(char_dict):
    list_of_char_dicts = []

    #Convert dict to list of dicts and sort
    for char, num in char_dict.items():
        list_of_char_dicts.append({'char':char, 'num':num})
    list_of_char_dicts.sort(reverse=True, key=sort_on)
    return list_of_char_dicts

    