import os
files = os.listdir("../../../folder-test-test")
directory = "../../../folder-test-test"

def deleteNcharsFromAllFilesInDirectory(directory, numberOfChars = 8):
 print(numberOfChars)
 for f in files:
   old_file = os.path.join(directory, f)
   new_file = os.path.join(directory, f[:-8] + '.txt')
   os.rename(old_file, new_file)

deleteNcharsFromAllFilesInDirectory("C:/Users/suppo/Desktop/folder-test-test")
