n = 10
for i in range(1, n+1) :
    print("*"*i)

for j in range(1, n+1) :
    for k in range(1, j+1) :
        print(k, end="")
    print("")

