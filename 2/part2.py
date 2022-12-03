import re
with open("input.txt", "r") as f:
    print(sum(map(lambda a: (([[3,1,2],[a[0],a[0],a[0]],[2,3,1]][a[1]][a[0]-1]) + a[1]*3), map(lambda s: [ord(s[0])%4, ord(s[2])%4], re.findall(re.compile("([A-C]\s?[X-Z])"), str(f.read()))))))
