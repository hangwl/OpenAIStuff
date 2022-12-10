import os

print('Start')
# specify the directory where the files are located
directory = r"C:\Users\HangWei\Desktop\Data Science\3. Python\8. Advanced Stastical Methods\2. sklearn\Practical Example"

# get a list of all the files in the directory
files = os.listdir(directory)
print(files)

# loop through each file in the directory
for file in files:
    # get the file's current name and split it by the '+' character
    current_name = file.split('+')

    # create the new name by joining the file's name parts with an empty space
    new_name = ' '.join(current_name)
    print(new_name)

    # rename the file with the new name
    old = os.path.join(directory, file)
    new = os.path.join(directory, new_name)
    os.rename(old, new)
