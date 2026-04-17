sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
char_count = len(sentence)

print("\n--- Text Analysis ---")
print(f"Original text:  {sentence}")
print(f"Uppercase:      {sentence.upper()}")
print(f"Lowercase:      {sentence.lower()}")
print(f"Character count: {char_count}")
print(f"Word count:      {word_count}")