import re


def findWordsWithAdjacentVowels(input):
    # Find words with two adjacent vowels
    pattern = r'\b\w*[aeiouAEIOU]{2}\w*\b'
    words_with_adjacent_vowels = re.findall(pattern, input)

    return words_with_adjacent_vowels


if __name__ == "__main__":
    try:
        # Read input from User (each line contains a single word)
        input_text = input("Enter words (one word per line): ")
        words = input_text.splitlines()

        # Looping each word for adjacent vowel
        for word in words:
            adjacent_vowel_words = findWordsWithAdjacentVowels(word)
            if adjacent_vowel_words:
                print(f"Words with adjacent vowels in '{word}': {', '.join(adjacent_vowel_words)}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
