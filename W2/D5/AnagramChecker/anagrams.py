# anagrams.py

from anagram_checker import AnagramChecker

checker = AnagramChecker("sowpods.txt")

def main():
    while True:
        print("\n Anagram Checker Menu")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break
        elif choice == "1":
            word = input("Enter a word: ").strip()

            if not word.isalpha():
                print("Error: Please enter a word with only alphabetic characters.")
                continue

            if " " in word or len(word.split()) > 1:
                print("Error: Only one word is allowed.")
                continue

            is_valid = checker.is_valid_word(word)
            anagrams = checker.get_anagrams(word)

            print(f"\nYOUR WORD: \"{word.upper()}\"")
            print("This is a valid English word." if is_valid else "This is NOT a valid English word.")
            print("Anagrams for your word:", ", ".join(anagrams) if anagrams else "None found.")
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
