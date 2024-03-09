from question_b import get_sum_of_evens

def main():
    while True:
        user_input = input("Enter a number to sum evens (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            num = int(user_input)
            total = get_sum_of_evens(num)
            print(f"The sum of even numbers up to {num} is: {total}")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
