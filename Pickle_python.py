# Python Pickle functions
# dump():- This function is called to serialize an object
# load():- This function is called to deserialize an object

import pickle

list = [
    10, 20, 30, 40]
file = open("writedata.txt", "wb")

pickle.dump(list, file)

file.close()

# file = open("writedata.txt", "rb")
# l=pickle.load(file)
# print(l)