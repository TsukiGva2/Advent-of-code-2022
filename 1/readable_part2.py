import re

with open("input.txt", "r") as f:
    print(sum(sorted(
            map(
                lambda s: sum(
                    [int(x) for x in s.splitlines()]
                    ),
                (re.compile(r"((?:[0-9]+\n?)+)(?!\n^$)", re.MULTILINE)).findall(str(f.read()))
                )
            )[-3:]
        )
    )

