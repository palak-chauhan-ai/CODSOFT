print("===== SIMPLE CALCULATOR =====")

while True:
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                print(f"Result = {result}")

            elif choice == '2':
                result = num1 - num2
                print(f"Result = {result}")

            elif choice == '3':
                result = num1 * num2
                print(f"Result = {result}")

            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"Result = {result}")

        except ValueError:
            print("Please enter valid numbers.")

    else:
        print("Invalid choice!")

    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using Calculator!")
        break