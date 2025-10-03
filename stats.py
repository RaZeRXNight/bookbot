
# Gets the word count of the inputted string.
def get_word_count(file_content=str):
    return len(file_content.split())

# Creates a dictionary of characters, with their values being related to their amount of occurances.
def get_char_dict(file_content=str):
    temp_dict = {}
    for word in file_content.split():
        for char in word: # char represents a singular letter in the word.
            key = char.lower()
            if key in temp_dict:
                temp_dict[key]+= 1
            else:
                temp_dict[key] = 1
            
    return temp_dict

# Sorts the inputted Array, by it's value and returns a new sorted list.
def sort_char_dict(char_array=dict):
    first_List = []
    
    # Appends all Inputted Characters to first_List.
    for char in char_array:
        first_List.append({"char": char, "num": char_array[char]})
        
    
    # Restructures first_List into a new temp_list, going from highest to smallest.
    
    return sorted(first_List, key=lambda char: char["num"], reverse=True)