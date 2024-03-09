from question_c import get_fahrenheit

def main():
    print("Celsius to Fahrenheit Conversion Table")
    print("Celsius | Fahrenheit")
    print("--------------------")
    for celsius in range(0, 21):
        fahrenheit = get_fahrenheit(celsius)
        print(f"{celsius:<7} | {fahrenheit:>10}")

if __name__ == "__main__":
    main()
