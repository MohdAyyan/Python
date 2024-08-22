def printnTo1(n):
    if n== 0:
        return;
    print(n);
    printnTo1(n-1);

print(printnTo1(5));