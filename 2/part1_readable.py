import re

def main():
    text = ""
    with open("input.txt", "r") as f:
        text = str(f.read())

    matches = re.findall(re.compile("([A-C]\s?[X-Z])"), text)

    moves = list(map(lambda s: [ord(s[0])%4, ord(s[2])%4+1], matches))
    score = sum(map(lambda a: (a[1] + [3,6,0][(a[1]-a[0])]), moves))
    print(score)

if __name__ == "__main__":
    main()

