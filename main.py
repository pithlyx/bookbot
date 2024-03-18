def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def parse_text(content):
    letters = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    words = content.lower().split()
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
    return letters, len(words)

def book_report(filepath, sort_by="occ"):
    letter_count, word_count = parse_text(read_file(filepath))
    sort_key = (lambda item: item[1]) if sort_by == "occ" else (lambda item: item[0])
    sorted_letter_count = sorted(letter_count.items(), key=sort_key, reverse=True)
    max_length = max(len(str(count)) for _, count in sorted_letter_count)

    print(f"--- Report of {filepath} ---")
    print(f"Word Count: {word_count}")
    print("Letter Occurrences:")
    for i, (letter, count) in enumerate(sorted_letter_count, start=1):
        print(f"{letter}: {count:<{max_length}}", end="\n" if i % 5 == 0 else "    ")
    if len(sorted_letter_count) % 5 != 0:
        print()

if __name__ == '__main__':
    book = "books/frankenstein.txt"
    book_report(book, "occ")
