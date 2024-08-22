with open("08_FileHandiling\demo.txt","r") as f:
    data = f.read()
    print(data)
with open("08_FileHandiling\demo.txt","a") as f:
    f.write("lorem ipsum dollor modi");
# w overwrite the file
# And a add the file add the start 