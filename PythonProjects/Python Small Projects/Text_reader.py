

def main():
    province = read_list("provinces.txt")
    print(province)

    province.pop(0)

    province.pop()

    for i in range(len(province)):
        if province[i] == "AB":
            province[i] = "Alberta"

    count = province.count("Alberta")

    print()
    print(f'Alberta occurs {count} times in the modified list.')



def read_list(filename):
    text_list = []

    with open(filename, 'rt') as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    
    return text_list


main()

