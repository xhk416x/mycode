##reads dracula from file and prints different conditions

search = "vampire"
count = 0

with open("dracula.txt", "r") as book:
    for line in book:
        if search in line.lower():
            print(line)
            count += 1
            with open("vampirecount.txt", "a") as countfile:
                countfile.write(line)
print(count)