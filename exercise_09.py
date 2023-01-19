words = []
while len(words) < 5:
    word = input("Enter a word: ")
    words.append(word)
print("Words:", words)
result = " ".join(words)
print("One string:", result)