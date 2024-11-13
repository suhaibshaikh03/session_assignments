num : int = int(input("Enter a number\n"))
if num >= 100:
    exit()
else:
    while num < 100:
        num = num * 2
        print(num , end=" ")