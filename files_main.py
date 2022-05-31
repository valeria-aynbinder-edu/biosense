if __name__ == '__main__':


    alice_count = 0
    img = "/Users/valeria/Documents/machine-learning-types.png"
    # with open("/Users/valeria/src/biosense/alice_in_wonderland.txt", "r") as file_handle:
    with open(img, 'rb') as file_handle:
        # content = file_handle.read()
        for i, line in enumerate(file_handle):
            print(line)

    # print(alice_count)



    # print(len(content))

