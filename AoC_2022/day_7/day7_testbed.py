from day7_data import root_test
# cd_count = [i for i in root_test.splitlines() if "cd" in i]
# cd_count = [1 for i in cd_count if ".." not in i]
# print(sum(cd_count))
tree = []
directory = []
child = False
toggle = False


def go_deeper(element):
    print(directory)
    print(tree)
    for el in element:
        if type(el) == list:
            if tree_element[0][4:] == directory[0][5:]:
                if "dir" in segment:
                    tree_element.extend([[segment]])
                else:
                    tree_element.extend([int(segment.split(" ")[0])])
            else:
                pass
        else:
            pass
            # go_deeper(el)


for segment in root_test.splitlines():
    if len(directory) == 0 and not child:
        directory.append(segment)
        tree.append(segment)
    elif "$ cd" in segment:
        child = True
        directory.clear()
    elif "$ ls" in segment and not child:
        pass
    elif "dir" in segment and not child:
        tree.append([segment])
    elif not child:
        tree.append(int(segment.split(" ")[0]))
    if child:
        # print("I am a child", segment, directory)
        if "$ ls" in segment:
            pass
        elif "$ cd" in segment:
            if len(directory) == 0:
                directory.append(segment)
            else:
                directory.clear()
        else:
            # go_deeper(segment)
            # print(directory)
            for tree_element in tree:
                # go_deeper(tree_element)
                if type(tree_element) == list:
                    # print(segment, directory)
                    go_deeper(tree_element)
                    if tree_element[0][4:] == directory[0][5:]:
                        if "dir" in segment:
                            tree_element.extend([[segment]])
                        else:
                            tree_element.extend([int(segment.split(" ")[0])])
                    else:

                        # tree_element.extend([segment])
                        pass
                        # print(segment)
                else:
                    # print(segment, directory)
                    # print("Hi")
                    pass


print(tree)
# print(any(isinstance(el, list) for el in tree))



