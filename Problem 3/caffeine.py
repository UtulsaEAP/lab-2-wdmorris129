
def caffeine():
    caffeine_mg = float(input())

    caffeineLevel_6 = caffeine_mg / 2
    caffeineLevel_12 = caffeineLevel_6 / 2
    caffeineLevel_24 = caffeineLevel_12 / 2
    
    print(caffeineLevel_6, caffeineLevel_12, caffeineLevel_24)
    
if __name__ == "__main__":
    caffeine()