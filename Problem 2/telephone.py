"""Will Morris
Friday Afternoon Lab"""

def telephone():
    phone_number_str = input()

    if phone_number_str.isdigit() and len(phone_number_str) == 10:

        phone_number = int(phone_number_str)

  
        area_code = phone_number // 10000000
        prefix = (phone_number % 10000000) // 10000
        line_number = phone_number % 10000


        print(f'({area_code}) {prefix}-{line_number}')
    else:
        print("Please enter a 10 digit #")
   


if __name__ == "__main__":
    telephone()