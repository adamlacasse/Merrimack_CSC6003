import re
from collections import Counter

def display_menu():
    print("===Edit Menu===")
    print("1: Top 5 most common words")
    print("2: Single Word Frequency")
    print("3: Replace a word")
    print("4: Add Text")
    print("5: Delete Text")
    print("6: Highlight Text")
    print("=============")

def all_word_count(text):
    words = re.findall(r'\b\w+\b', text.lower())
    most_common = Counter(words).most_common(5)
    for word, count in most_common:
        print(f"{word.upper()} appears {count} times")

def single_word_count(text, word):
    count = text.lower().split().count(word.lower())
    print(f"{word.upper()} appears {count} times in the text")

def replace_word(text, target, replacement):
    count = len(re.findall(rf'\b{re.escape(target)}\b', text, re.IGNORECASE))
    updated_text = re.sub(rf'\b{re.escape(target)}\b', replacement, text, flags=re.IGNORECASE)
    print(f"{count} words replaced with {replacement.upper()}")
    return updated_text

def add_text(text, new_text):
    return text + "\n" + new_text

def delete_text(text, target):
    updated_text = re.sub(rf'\b{re.escape(target)}\b', '', text, count=1, flags=re.IGNORECASE)
    print(f"Deleted the first instance of {target}")
    return updated_text

def highlight_word(text, word):
    highlighted_text = re.sub(rf'\b{re.escape(word)}\b', f"[{word.upper()}]", text, flags=re.IGNORECASE)
    print("Highlighted the word in the text")
    return highlighted_text

def main():
    file_path = "changeme.txt"
    try:
        with open("changeme.txt", 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return

    while True:
        display_menu()
        choice = input(">>input: ").strip()
        
        if choice == "1":
            all_word_count(text)
        elif choice == "2":
            word = input(">>input Word: ").strip()
            single_word_count(text, word)
        elif choice == "3":
            target = input(">>input target word: ").strip()
            replacement = input(">>input replacement: ").strip()
            text = replace_word(text, target, replacement)
        elif choice == "4":
            new_text = input(">>input text to add: ").strip()
            text = add_text(text, new_text)
        elif choice == "5":
            target = input(">>input text to delete: ").strip()
            text = delete_text(text, target)
        elif choice == "6":
            word = input(">>input word to highlight: ").strip()
            text = highlight_word(text, word)
        else:
            print("Invalid choice. Please try again.")
            continue

        if choice in ["3", "4", "5", "6"]:
            save = input("Do you want to save changes? (yes/no): ").strip().lower()
            if save == "yes":
                with open(file_path, 'w') as file:
                    file.write(text)
                print("Changes saved.")

        exit_program = input("Do you want to exit? (yes/no): ").strip().lower()
        if exit_program == "yes":
            break

main()
