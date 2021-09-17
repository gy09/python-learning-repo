fileHandle = open("File1", "w")
print(fileHandle.writable())
print(fileHandle.writelines("Hey There this is my first file \n Hope this will go fine and \n I will be able to "
                            "create one"))
fileHandle.close