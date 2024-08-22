phones = {
    "John" : 982628,
    "Ria" : 4526279,
    "Joy" : 1234567,
}
print(phones)
print(len(phones));
#acces items of dict
print(phones["John"])
print(phones.get("John"))
print(phones.keys())
#changebale
for x,y in phones.items():
    print(x,y)