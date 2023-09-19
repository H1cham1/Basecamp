Width = int(input(""))
Height = int(input(""))


for i in range(Height):
    for j in range(Width):
        num = (i*Width+j) % 10 
        print(num, end=' ')
    print()