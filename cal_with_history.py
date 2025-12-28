HISTORY_FILE = 'history.txt'

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        return "No history available."
    else :
        for lines in reversed(lines):
            print(lines.strip())
    file.close()


def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History cleared.')

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + " =   " + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter an equation in the format: number operator number")
        return
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero")
            return 
        result = num1 / num2
    else:
        print("Invalid operator. Please use one of +, -, *, /")
        return 
    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)
    return 

def main():
    print('__SIMPLE CALCULATOR__')
    while True:
        user_input = input("Enter calculation (+, -, *, /) (or 'history' to view history, 'clear' to clear history, 'quit' to exit): ")
        if user_input == 'exit':
            print('Goodbye!')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
        
main()