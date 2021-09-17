fileHandle = open("EMPFILE","a")
print(fileHandle.writable())
print(fileHandle.writelines("\nHi There \n WhatsUp \n How you Doing \n Gaurav is my name "))
print(fileHandle)

fileHandle.close()