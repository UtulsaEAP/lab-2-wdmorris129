
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())

    num_product = (num1 * num2 * num3 * num4)
    num_avg = ((num1 + num2 + num3 + num4) / 4 )
    
    print(f'{num_product:.0f}', f'{num_avg:.0f}')
    print(f'{num_product:.3f}', f'{num_avg:.3f}')

if __name__ == "__main__":
    simple_stats()