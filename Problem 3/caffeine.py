
def caffeine():
    caffeine_mg = float(input())

    caffeineLevel_6 = caffeine_mg / 2 
    caffeineLevel_12 = caffeineLevel_6 / 2
    caffeineLevel_24 = caffeineLevel_12 / 2
    
    # mg = 'mg'
    # print(caffeineLevel_6, caffeineLevel_12, caffeineLevel_24)
    # print(f'{caffeineLevel_6:.2f}' , f'{caffeineLevel_12:.2f}' , f'{caffeineLevel_24:.2f}')

    print(f'{"After 6 hours: {a} mg".format(a = caffeineLevel_6):.2f}')
    print(f'{"After 12 hours: {a} mg".format(a = caffeineLevel_12):.2f}')
    print(f'{"After 24 hours: {a} mg".format(a = caffeineLevel_24):.2f}')
   
    print(f'{"After 6 hours: %s %caffeineLevel_6+:.2f}')
    print(f'{"After 12 hours: {a} mg".format(a = caffeineLevel_12):.2f}')
    print(f'{"After 24 hours: {a} mg".format(a = caffeineLevel_24):.2f}')

if __name__ == "__main__":
    caffeine()