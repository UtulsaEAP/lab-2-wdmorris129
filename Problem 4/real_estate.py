"""Will Morris
Friday Afternoon Lab"""
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())

    change_price = current_price - last_month_price
    mortage = (current_price * 0.051) / 12

    # print(f'{current_price:.2f}', f'{change_price:.2f}', f'{mortage:.2f}')

    print("This house is ${:.2f}.".format (current_price)\
        , "The change is ${:.2f} since last month.".format (change_price) \
        , "The estimated monthly mortgage is ${:.2f}.".format(mortage))
   
if __name__ == "__main__":
    real_estate()