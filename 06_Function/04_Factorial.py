def factorial(n):
    ans = 1;
    if n == 0:
        ans = 1;
    else:
        for i in range(1,n+1):
         ans *= i;
    return ans;

factans = factorial(5);
print(factans);

