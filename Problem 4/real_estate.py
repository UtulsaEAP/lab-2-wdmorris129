
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())

    change_price = current_price - last_month_price
    mortage = (current_price * 0.051) / 12

    # print(f'{current_price:.2f}', f'{change_price:.2f}', f'{mortage:.2f}')

    print("This house is ${a}.".format (a = f'{current_price:.2f}'), "The change is ${b} since last month.".format \
          (b = f'{change_price:.2f}'), "The estimated monthly mortgage is ${c}.".format (c = f'{mortage:.2f}'))
   
if __name__ == "__main__":
    real_estate()