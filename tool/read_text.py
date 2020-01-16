def read_text(filename):
    with open("./data/" + filename, "r") as f:
        return f.readlines()


if __name__ == '__main__':
    data_list = []
    for code in read_text("code"):
        code = code.strip('\n')
        data_list.append(code)
    print(data_list)
