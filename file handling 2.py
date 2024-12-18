with open('infile') as infile:
    lines=0
    characters=0
    for line in infile:
        lines=lines+1
        characters += sum(len(word) for word in wordslist)
print(lines)
print(characters)
