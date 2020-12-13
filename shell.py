import basic

# while True:
#     text = input("begir ")


tokens = {
    "&B": " > ",
    "&BM": " >= ",
    "&K": " < ",
    "&KM": " <= ",
    "MM": " == ",
    "Benevis": "print",
    "Jam": " + ",
    "YekiBala": " +=1 ",
    "Kam": "-",
    "YekiPain": " -=1 ",
    "Zarb": " * ",
    "Taghsim": " / ",
    "Baghimonde": " % ",
    "agar": "if ",
    ":": " : ",
}


while True:
    stri = input()
    string = stri.split()
    do = ""

    if do == "fuck":
        break
    result = basic.run("<stdin>", string)
    print(result)
    try:
        for i in string:
            if i == "Begir":
                x = int(input())
                continue
            if i == "('%d',x)":
                continue
            if i in tokens:
                # import ipdb; ipdb.set_trace()
                # eval(tokens[i])
                do += tokens[i]
            else:
                do += i

        # print("do si " , do)
        # print(do)
        exec(do)
    except EOFError:
        print("fuck you sina")

