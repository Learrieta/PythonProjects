import csv

from family_history import NAME_INDEX



def main():
    NUMBER_INDEX = 0
    NAME_INDEX = 1


    student_dict = read_dict("students.csv",NUMBER_INDEX)

    user_input = input("Please enter an I-Number (xxxxxxxxx): ")
    user_input = user_input.replace("-","")

    if user_input in student_dict:
        value = student_dict[user_input]
        name = value[NAME_INDEX]
        print(name)
    else:
        print("No such student ")


def read_dict(filename, key):
    dictionary = {}

    with open(filename,"rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            key_file = row[key]
            dictionary[key_file] = row
        
    return dictionary




    

if __name__ == "__main__":
    main()


    






main()

        




