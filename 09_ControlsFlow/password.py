password = "xyxncbksj@1233";
if len(password) < 6:
    print("Weak");
elif(len(password) <= 10):
    print("Medium");
else:
    print("Hard");