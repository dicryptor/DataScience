import os, shutil

birds = []

for root, dirnames, filenames in os.walk("C:\\Users\\wonderlander\\Downloads\\CUB_200_2011\\CUB_200_2011\\images"):
    for filename in filenames:
        if filename.endswith('.jpg'):
            # matches.append(os.path.join(root, filename))
            # birds.append(filename)
            old = os.path.join(root,filename)
            new = os.path.join("C:\\Users\\wonderlander\\Downloads\\CUB_200_2011\\", filename)
            shutil.move(old, new)

# print(len(birds))