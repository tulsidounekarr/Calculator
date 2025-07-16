import sys
print("Python executable:", sys.executable)

import time
import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return Fore.RED + "❌ Error: Division by zero is undefined."
    return a / b

# Get validated number input from user
def get_number(prompt):
    while True:
        try:
            value = float(input(Fore.CYAN + prompt))
            return value
        except ValueError:
            print(Fore.RED + "🚫 Invalid input! Please enter a valid number.")

# Display welcome message with ASCII art
def show_banner():
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "=" * 50)
    print(Fore.GREEN + Style.BRIGHT + "     🧮  Python CLI Calculator")
    print(Fore.YELLOW + Style.BRIGHT + "=" * 50)
    print(Fore.BLUE + f"   📅 Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(Fore.YELLOW + "=" * 50 + "\n")
    time.sleep(1)

# Main program loop
def main():
    show_banner()

    while True:
        print(Fore.MAGENTA + "\nSelect an operation:")
        print("1. ➕ Add")
        print("2. ➖ Subtract")
        print("3. ✖️ Multiply")
        print("4. ➗ Divide")
        print("5. 🚪 Exit")

        choice = input(Fore.CYAN + "\nEnter choice (1-5): ")

        if choice == '5':
            print(Fore.BLUE + "\n👋 Thanks for using the calculator. Goodbye!\n")
            break

        if choice not in {'1', '2', '3', '4'}:
            print(Fore.RED + "❗ Invalid choice! Please select from 1 to 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        print(Fore.YELLOW + "\n🔍 Processing your request...\n")
        time.sleep(1)

        if choice == '1':
            result = add(num1, num2)
            op = "Addition"
        elif choice == '2':
            result = subtract(num1, num2)
            op = "Subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            op = "Multiplication"
        else:
            result = divide(num1, num2)
            op = "Division"

        print(Fore.GREEN + f"✅ {op} Result: {result}")

        again = input(Fore.CYAN + "\n🔁 Do you want to perform another operation? (y/n): ").strip().lower()
        if again != 'y':
            print(Fore.BLUE + "\n🎉 Session Ended. Have a great day!\n")
            break

# Run the calculator
if __name__ == "__main__":
    main()
