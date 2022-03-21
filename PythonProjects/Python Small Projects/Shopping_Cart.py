import csv
from datetime import datetime


def main():
    try:

        PRODUCT_NUMBER_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2
        KEY_COLUMN_INDEX = 0
        QUANTITY_INDEX = 1
        
        

        products_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)

        print("Inka Emporium")
        print()
        added_q = 0
        price_due = 0

        with open("request.csv","rt") as request_file:
            reader_one = csv.reader(request_file)
            next(reader_one)
            for row in reader_one:
                key = row[KEY_COLUMN_INDEX]
                quantity = int(row[QUANTITY_INDEX])
                if key in products_dict:
                    value = products_dict[key]
                    name = value[PRODUCT_NAME_INDEX]
                    price = float(value[PRODUCT_PRICE_INDEX])
                    print(f'{name}: {quantity} @ {price}')
                    added_q += quantity 
                    price_due += quantity * price
        
        tax_sale = 0.06 * price_due
        current = datetime.now()
        
                    
        print()
        print('Number of Items:', added_q)
        print(f'Subtotal: ${price_due:.2f}')
        print(f'Sales Tax: ${tax_sale:.2f}')
        print("Thank you for shopping at the Inka Emporium")
        print(f"{current:%a %b  %w  %I:%M:%S %Y}")
        
    
    except (FileNotFoundError, PermissionError) as error:
        print("Error: missing file")
        print(error)
        
    
    except ValueError as val_err:
        print("Error: ", val_err)
    
    except KeyError as error:
        print(f"Error: line {error} ")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV  file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
            
    return dictionary


if __name__ == "__main__":
    main()



