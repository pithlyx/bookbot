def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def parse_text(content, word_min_length=4):
    words = content.lower().split()
    
    letter_tracker = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    word_tracker = {}
    for word in words:
        if len(word) < word_min_length:
            continue
        elif word in word_tracker:
            word_tracker[word] += 1
        elif word not in word_tracker:
            word_tracker[word] = 1
        for letter in word:
            if letter in letter_tracker:
                letter_tracker[letter] += 1
    return  len(words), word_tracker, letter_tracker

def print_tuples(tuple_list, filter_func=None, sort_func=None, reverse=True, top_n=None, items_per_line=5, spacing=10):
    if filter_func:
        tuple_list = filter(filter_func, tuple_list)
    if sort_func:
        tuple_list = sorted(tuple_list, key=sort_func, reverse=reverse)
    if top_n:
        tuple_list = tuple_list[:top_n]

    # Initialize a counter to keep track of the number of items printed on the current line
    counter = 0
    line = ""  # Initialize an empty string to build the current line

    for t in tuple_list:
        # Format the tuple and add it to the line with the specified spacing
        line += f"{t[0]}: {t[1]:<{spacing}}"
        counter += 1
        
        # When the counter reaches the specified number of items per line, print the line and reset
        if counter == items_per_line:
            print(line.strip())
            line = ""  # Reset the line
            counter = 0  # Reset the counter

    # Print any remaining items in the line after exiting the loop
    if line:
        print(line.strip())

        
        
def book_report(filepath):
    word_count, word_tracker, letter_tracker = parse_text(read_file(filepath))
    
    print(f"--- Report of {filepath} ---")
    print(f"Words: {word_count} | Unique Word Count: {len(word_tracker)}")
    print(f"Letters: {sum(letter[1] for letter in letter_tracker.items())} | ")
    print("Averages:")
    print(f"")
    print(f"Letter Count: {len(letter_tracker)} | Avg. Word Length: {sum(len(word)*word_tracker[word] for word in word_tracker)/sum(word_tracker.values()):.2f} | Avg. Letter Occurrence: {sum(letter_tracker.values())/len(letter_tracker):.2f}")
    print("--- Letters ---")
    print("All letters:")
    print_tuples(letter_tracker.items())
    print("5 Most common letters:")
    print_tuples(letter_tracker.items(), sort_func=lambda item: item[1], top_n=5)
    print("5 Least common letters:")
    print_tuples(letter_tracker.items(), sort_func=lambda item: item[1], reverse=False, top_n=5)
    print("--- Words ---")
    print("5 Most common words:")
    print_tuples(word_tracker.items(), sort_func=lambda item: item[1], top_n=5)
    print("5 Least common words:") 
    print_tuples(word_tracker.items(), sort_func=lambda item: item[1], reverse=False, top_n=5)
    

if __name__ == '__main__':
    book = "books/frankenstein.txt"
    book_report(book)
