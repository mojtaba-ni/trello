def connected_to(u, c):

    return -1


n = int(input())

accept = [0] * n

DFA = [[]] * n  # This is The DFA
# print(DFA)


for i in range(n):
    l = input().split(" ")
    a, b = map(int, l[:2])
    DFA[a].append((b, c))

# put an end to the dfa
k = int(input())  # how many ends it will have ?
for i in range(k):
    x = int(input())
    accept[x] = 1

while True:
    r = input()
    if r == "EOF":
        break
    a = int(input())
    for i in range(len(r)):
        c = r[i]
        a = connected_to(a, r[i])
        if a == -1:
            print("NO")
            break
        if(i == r.length()-1){
            if(accept[a]==1)
                print("YES")
            else:
                print("NO")

