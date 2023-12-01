from day7_data import root, root_test

root_list = [segment for segment in root_test.splitlines()]
tree = []
temp = []
directory = []
count = 0

for i in range(len(root_list))[:6]:
    # print(root_list[i])
    if "$ cd" in root_list[i]:

        tree.append(directory)
        directory.clear()
        directory.extend([root_list[i]])
        # print(temp)
    elif "dir" in root_list[i]:
        directory.extend([[root_list[i]]])
        # print(temp)
    else:
        if root_list[i] == "$ ls":
            pass
        else:
            data = [root_list[i].split(" ")]
            directory.append(int(data[0][0]))
            print(data)
print(root_list[:])
print(directory)
print(tree)
