def get_word_count(text):
    words = text.split()
    return len(words)

def char_count(string):
    count = {}
    for char in string:
        # Convert character to lowercase before counting
        char = char.lower()
        count[char] = count.get(char, 0) + 1
    return count

def sort_on(count):
    return count["num"]


def sorted_list(char_dict):
    # Create a list to hold our dictionaries
    result = []
    
    # Converts each key-value pair to a dictionary and adds to the list
    for char, num in char_dict.items():
        result.append({"char": char, "num": num})

    result.sort(reverse=True, key=sort_on)

    
    return result