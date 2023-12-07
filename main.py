def leap_year_checker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


while True:
    given_year = input("Please input a year (type 'exit' to end): ")

    if given_year.lower() == 'exit':
        print("Exiting the leap year checker.")
        break  # Exit the loop if the user types 'exit'

    try:
        year = int(given_year)
        if leap_year_checker(year):
            print(f'{year} is a Leap Year')
            break  # Exit the loop if a leap year is entered
        else:
            print(f'{year} is Not a Leap Year. Please try again.')
    except ValueError:
        print("Invalid input. Please enter a valid year or type 'exit' to end.")
