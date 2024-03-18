def read_file(file_path):
    with open(file_path, "r") as file:  # Open the file in read mode
        return file.read()  # Return the entire content of the file

def parse_text(content, word_min_length=4):
    words = content.lower().split()  # Convert to lowercase and split into words
    
    # Initialize a tracker for each letter in the alphabet with a count of 0
    letter_tracker = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    word_tracker = {}  # Initialize an empty dictionary to track word occurrences
    
    for word in words:  # Iterate over each word in the text
        if len(word) < word_min_length:  # Skip words shorter than the minimum length
            continue
        # Increase the word count or add it to the dictionary if it's not already there
        word_tracker[word] = word_tracker.get(word, 0) + 1
        for letter in word:  # Iterate over each letter in the current word
            if letter in letter_tracker:  # Check if the letter is in the alphabet (ignores punctuation)
                letter_tracker[letter] += 1  # Increment the count for this letter
                
    # Return the total number of words, the word occurrences, and the letter occurrences
    return len(words), word_tracker, letter_tracker

def print_tuples(tuple_list, filter_func=None, sort_func=None, reverse=True, top_n=None, items_per_line=5, spacing=10):
    # Apply a filter to the tuple list if a filter function is provided
    if filter_func:
        tuple_list = filter(filter_func, tuple_list)
    # Sort the tuple list based on the provided sort function, if any
    if sort_func:
        tuple_list = sorted(tuple_list, key=sort_func, reverse=reverse)
    # Limit the number of items to display if top_n is specified
    if top_n:
        tuple_list = tuple_list[:top_n]

    counter = 0  # Initialize a counter for items per line
    line = ""  # Start with an empty line

    for t in tuple_list:
        # Add each tuple to the line, formatted with dynamic spacing based on the 'spacing' parameter
        line += f"{t[0]}: {t[1]:<{spacing}}"
        counter += 1
        
        # Check if the line has reached the specified number of items
        if counter == items_per_line:
            print(line.strip())  # Print the current line
            line = ""  # Reset the line for the next set of items
            counter = 0  # Reset the item counter

    if line:  # Print any remaining items in the line
        print(line.strip())

def book_report(filepath):
    # Parse the text to get the total word count, word occurrences, and letter occurrences
    word_count, word_tracker, letter_tracker = parse_text(read_file(filepath))
    
    # Print the header and overall statistics
    print(f"--- Report of {filepath} ---")
    print(f"Words: {word_count} | Unique Word Count: {len(word_tracker)}")
    print(f"Letters: {sum(letter[1] for letter in letter_tracker.items())} | ")
    print("Averages:")
    # Calculate and print averages for letter count, average word length, and average letter occurrence
    print(f"Letter Count: {len(letter_tracker)} | Avg. Word Length: {sum(len(word)*word_tracker[word] for word in word_tracker)/sum(word_tracker.values()):.2f} | Avg. Letter Occurrence: {sum(letter_tracker.values())/len(letter_tracker):.2f}")
    print("--- Letters ---")
    # Print all letters and their counts
    print("All letters:")
    print_tuples(letter_tracker.items())
    # Print the 5 most and least common letters
    print("5 Most common letters:")
    print_tuples(letter_tracker.items(), sort_func=lambda item: item[1], top_n=5)
    print("5 Least common letters:")
    print_tuples(letter_tracker.items(), sort_func=lambda item: item[1], reverse=False, top_n=5)
    print("--- Words ---")
    # Print the 5 most and least common words
    print("5 Most common words:")
    print_tuples(word_tracker.items(), sort_func=lambda item: item[1], top_n=5)
    print("5 Least common words:") 
    print_tuples(word_tracker.items(), sort_func=lambda item: item[1], reverse=False, top_n=5)

if __name__ == '__main__':
    book = "books/frankenstein.txt"
    book_report(book)
