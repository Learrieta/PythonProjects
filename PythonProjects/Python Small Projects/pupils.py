import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    students_list = read_compound_list("pupils.csv")

    oldest = oldest_to_youngest(students_list)
    print_list(oldest)
    print()

    sorted_list = given_name(students_list)
    print_list(sorted_list)
    print()

    monthly = birth_month(students_list)
    print_list(monthly)
    print()




def oldest_to_youngest(student_list):
    birthday = lambda birth : birth[BIRTHDATE_INDEX]

    oldest = sorted(student_list, key = birthday)

    return oldest


def given_name(student_list):

    def student_name(first):
        birth = first[GIVEN_NAME_INDEX]
        return birth
   

    sorted_list = sorted(student_list, key = student_name)

    return sorted_list

def birth_month(student_list):
    
    def extract_month(student):
        birthday_string = student[BIRTHDATE_INDEX]
        month_and_day = birthday_string[5:]
        return month_and_day
    
    sorted_list = sorted(student_list, key = extract_month)
    return sorted_list





def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(lists):
    
    for list in lists:
        print(list)
    print()


main()



