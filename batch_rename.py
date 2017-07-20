import os
path = 'test\\'
files = os.listdir(path)
# i = 1

for i, file in enumerate(files):
    print(file)
    new_name = 'test' + str(i).zfill(3) + '.jpg'
    print(new_name)
    os.rename(os.path.join(path, file), os.path.join(path, new_name))
