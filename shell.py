import basic
from tokens import tokens
# while True:
#     text = input("begir ")

tokens = tokens.tokens

def dodo():
    while True:
        stri = input()
        string = stri.split()
        do = ""

        if do == "fuck":
            break
        result = basic.run("<stdin>", string)
        try:
            for i in string:
                if i == "Begir":
                    x = int(input())
                    continue
                if i == "('%d',x)":
                    continue
                if i in tokens:
                    # import ipdb; ipdb.set_trace()
                    do += tokens[i]
                else:
                    do += i

            # print("do si " , do)
            # print(do)
            exec(do)
        except EOFError:
            print("an error happend")

