def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = int(input("Enter the operation choice (1-4): "))
            if operation < 1 or operation > 4:
                print("Invalid operation choice. Please choose a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if operation == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif operation == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif operation == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif operation == 4:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        
        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        while again not in ["yes", "no"]:
            again = input("Invalid input. Please enter yes or no: ").lower()
        if again == "no":
            print("Thanks for using the calculator!")
            break

def main():
    calculator()

if __name__ == "__main__":
    main()
