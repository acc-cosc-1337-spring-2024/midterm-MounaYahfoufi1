from question_d import use_global, global_var

def main():
    print(f"Global variable before calling use_global: {global_var}")
    use_global()
    print(f"Global variable after calling use_global: {global_var}")

if __name__ == "__main__":
    main()
