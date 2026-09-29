word = input("Enter the word to search: ")
count = 0

file = open("sample.txt", "r")

for line in file:
    if word in line:
        count += 1

file.close()

print("Number of lines containing the word:", count)