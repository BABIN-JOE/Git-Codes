def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num_count = int(input("How many numbers? "))
        numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num_count)]

        if choice == '1':
            print(f"Result: {add(numbers)}")

        elif choice == '2':
            print(f"Result: {subtract(numbers)}")

        elif choice == '3':
            print(f"Result: {multiply(numbers)}")

        elif choice == '4':
            print(f"Result: {divide(numbers)}")
    else:
        print("Invalid input")

# Run the calculator
calculator()
