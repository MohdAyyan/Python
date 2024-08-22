def sum(n):
    if(n == 0):
        return 1;
    ans = n + sum(n-1);
    return ans;

n = sum(5);
print(n);