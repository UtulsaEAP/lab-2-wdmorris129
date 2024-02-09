def telephone():
    # phone_number = int(input())
    
    # areaCode = phone_number // 1000000000
    # firstPart = ((phone_number % 1000000000)// 10000)
    # secondPart = (phone_number % 10000)

    # print(f'{(areaCode)}  {firstPart}-{secondPart}')

    # Read input phone number as a string
    phone_number_str = input()

# Check if the input is a 10-digit number
    if phone_number_str.isdigit() and len(phone_number_str) == 10:
    # Convert the input string to an integer
        phone_number = int(phone_number_str)

    # Extract area code, prefix, and line number
        area_code = phone_number // 10000000
        prefix = (phone_number % 10000000) // 10000
        line_number = phone_number % 10000

    # Output in the specified format
        print(f'({area_code}) {prefix}-{line_number}')
    else:
        print("Invalid input. Please enter a 10-digit phone number.")
   


if __name__ == "__main__":
    telephone()