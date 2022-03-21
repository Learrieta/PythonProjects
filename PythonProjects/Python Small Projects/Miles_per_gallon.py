def main():
    start_miles = float(input("Enter the first odometer reading (miles): "))
    end_miles = float(input("Enter the second odometer reading (miles): "))
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    lpl100k = lpl100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{lpl100k:.2f} liters per 100 kilometers")




def miles_per_gallon(start_miles, end_miles, amount_gallons):
    mpg = abs(end_miles - start_miles) / amount_gallons
    return mpg

def lpl100k_from_mpg(mpg):
    lpl100k = 235.215 / mpg
    return lpl100k


main()


