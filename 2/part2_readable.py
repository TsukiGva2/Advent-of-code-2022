import re

def main():
    text = ""
    with open("input.txt", "r") as f:
        text = str(f.read())

    matches = re.findall(re.compile("([A-C]\s?[X-Z])"), text)

    moves = list(map(lambda s: [ord(s[0])%4, ord(s[2])%4], matches))
    score = sum(map(lambda a: (([[3,1,2],[a[0],a[0],a[0]],[2,3,1]][a[1]][a[0]-1]) + a[1]*3), moves))
    print(score)

if __name__ == "__main__":
    main()

