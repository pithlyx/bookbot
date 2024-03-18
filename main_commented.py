
def read_file(file_path):
    with open(file_path, "r") as file: # Open the file in read mode
        return file.read() # Return the content of the file

def parse_text(content):
    letters = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"} # Create a dictionary with all letters
    words = content.lower().split() # Split the text into words and convert to lowercase
    for word in words: # Iterate over each word in words
        for letter in word: # Iterate over each letter in the word
            if letter in letters: # If the letter is in the dictionary
                letters[letter] += 1 # Increment the count of the letter
    return letters, len(words) # Return the dictionary and the number of words
    

def book_report(filepath, sort_by="occ"):
    letter_count, word_count = parse_text(read_file(filepath)) # Parse the text and count the letters
    # | Define the sort_key function based on the value of `sort_by`
    # | lambda functions work like a function, but are defined in-line
    # | `lambda` is a keyword that defines an anonymous function
    # | The function takes an argument `item` and returns `item[1]` or `item[0]` based on the value of `sort_by`
    # | so this is equivalent to:
    # | def sort_key(item):
    # |     if sort_by == "occ":
    # |         return item[1]
    # |     else:
    # |         return item[0]
    sort_key = (lambda item: item[1]) if sort_by == "occ" else (lambda item: item[0])
    # | Sort the dictionary by the value of the items
    # | `sorted` sorts a list based on a value using the `sort_key` function
    # | `dict.items()` returns a list of tuples with the key-value pairs of the dictionary
    # | `reverse=True` sorts the list in descending order
    # | in our case, each `item` is a tuple with the letter and the count
    # | so `item[1]` is the count and `item[0]` is the letter
    sorted_letter_count = sorted(letter_count.items(), key=sort_key, reverse=True) 
    
    # | Find the maximum character length of count for formatting
    # | `max` returns the maximum value of an iterable
    max_length = max(len(str(count)) for _, count in sorted_letter_count)

    # --- Report ---
    print(f"--- Report of {filepath} ---")
    print(f"Word Count: {word_count}")
    print("Letter Occurrences:")
    for i, (letter, count) in enumerate(sorted_letter_count, start=1):
        # Print letter and its count, aligning count using dynamic formatting
        # `{:<{max_length}}` formats `count` to be left-aligned within a space of `max_length`
        # `end="\n" if i % 5 == 0 else "    "` determines how to end the line with a new line every 5 values
        print(f"{letter}: {count:<{max_length}}", end="\n" if i % 5 == 0 else "    ") 
    if len(sorted_letter_count) % 5 != 0:
        print()  # Ensure ending with a newline if the list isn't divisible by 5


if __name__ == '__main__':
    book = "books/frankenstein.txt"
    book_report(book, "let")