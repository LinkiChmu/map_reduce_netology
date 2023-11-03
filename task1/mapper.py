import sys

headers = input()

for line in sys.stdin:
    request = line.strip().split(",")[0]
    for word in request.split(" "):
        if not word.isdigit():
            print(f'{word},1')

