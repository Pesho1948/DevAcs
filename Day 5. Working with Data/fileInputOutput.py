#Use open func to open data by specifing a mode
"""
path= r"C:\\Users\\petar\\Desktop\\git token.txt"
file = open(path,"r")
print(file.read())
file.close()

"""

#Using with() func to deal with file closure

path_with = r'C:\Users\petar\Desktop\Admin key.txt'
with open(path_with, "a+") as data:
    data.write("\nHello world!")
    data.seek(0) # <- Changing the file point at the begginig of the text
    word_count = list()
    for word in data:
        word_count.append(word)
    print(len(word_count))
    #print(data.read())

#Match specific words

delete_str = "Hello"

#Take the lines in a list
with open(path_with, "r") as data:
    lines = data.readlines()

#Filter out the lines that contain delete_str
filter_lines = [line for line in lines if delete_str not in line] 

with open(path_with, "w") as data:
    data.writelines(filter_lines)

with open(path_with, "r") as data:
    print(data.read())