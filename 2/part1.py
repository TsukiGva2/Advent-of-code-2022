import re
with open("input.txt", "r") as f:
    print(sum(map(lambda a: (a[1] + [3,6,0][(a[1]-a[0])]), (map(lambda s: [ord(s[0])%4, ord(s[2])%4+1], re.findall(re.compile("([A-C]\s?[X-Z])"), f.read()))))))
