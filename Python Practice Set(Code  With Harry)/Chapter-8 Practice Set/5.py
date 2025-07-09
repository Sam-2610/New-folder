""" Write a python function to remove a given word from a list ad strip it at the same 
time.  """

def remove_word(word_list, word_to_remove):
    new_list = []
    for word in word_list:
        if word.strip() != word_to_remove.strip():
            new_list.append(word.strip())  # Add cleaned word if it's not the one to remove
    return new_list

print(remove_word(["apple", "banana", "cherry", "apple"], "apple"))