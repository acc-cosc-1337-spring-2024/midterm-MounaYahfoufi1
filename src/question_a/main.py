from question_a import use_local_variable

def main():
    num = 5  # Initialize num with a value
    print(f"Before calling 'use_local_variable', num is: {num}")
    use_local_variable(num)  # This will not change `num` because changes are local to the function.
    print(f"After calling 'use_local_variable', num is still: {num}")

if __name__ == "__main__":
    main()

