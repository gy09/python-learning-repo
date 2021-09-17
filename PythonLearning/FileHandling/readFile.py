fileHandle = open("File1","r")
print(fileHandle.readable())
print(fileHandle.read())
print(fileHandle.readlines())
print(fileHandle.readlines())

for cursor in fileHandle.readlines():
    print(cursor)


fileHandle.close()