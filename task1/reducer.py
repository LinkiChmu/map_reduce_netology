import sys

last_word, count = input().split(",")
count = int(count)

for line in sys.stdin:
    word, one = line.split(",")
    if word == last_word:
        count += int(one)
    else:
        print(f'{last_word},{count}')
        last_word, count = word, int(one)
print(f'{last_word},{count}')
