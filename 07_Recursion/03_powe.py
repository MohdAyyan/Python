def power(a,b):
    if(b == 0):
        return 1;
    ans = a *power(a,b-1);
    return ans;

print(power(2,3));