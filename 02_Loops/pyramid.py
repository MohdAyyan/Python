n = int (input("enter n : "));
for i in range(1,n+1):
    print(" "*(n-i),end="");
    for j in range(1,2 * n):
     print(j,end="")
    print()