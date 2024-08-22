s1 = {'a','b','c'};
s2 = {'d','e','a'};
print(s1,s2)
s3 = s1.union(s2);
print(s3)
s1.symmetric_difference_update(s2);
print(s1)