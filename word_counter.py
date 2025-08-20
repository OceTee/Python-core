# word count - input a string to output dictionary of word counts
def word_count(input_string):
    words = input_string.split()
    word_count_dict = {}
    
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in word_count_dict:
            word_count_dict[word] += 1 # Increment count if word already exists
        else:
            word_count_dict[word] = 1 # Initialize count to 1 if word is new
            
    return word_count_dict

# Example usage
if __name__ == "__main__":
    input_string = "Hello world hello"
    print(word_count(input_string))  # Output: {'hello': 2, 'world': 1}