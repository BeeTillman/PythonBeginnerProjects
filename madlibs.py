with open("story.txt", "r") as f: # opening the story.txt file in read (r) mode
    story = f.read()

words = set() # Using set instead of list so every element is unique (no duplicate words)
startOfWord = -1

targetStart = "<"
targetEnd = ">"

for i, char in enumerate(story):
    if char == targetStart:
        startOfWord = i

    if char == targetEnd and startOfWord != -1:
        word = story[startOfWord: i + 1]
        words.add(word)
        startOfWord = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
    
print("\nMadlib story created!\n")
print("Your story has been generated below\n")
print(story, "\n")