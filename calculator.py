def save_result(file_path):
    try:

        def to_sum(a, b):
            return a + b

        def to_substract (a, b):
            return a - b

        def to_multiple (a, b):
            return a * b

        def to_divide (a, b):
            return a / b

        def to_pow (a, b):
            return a ** b


        num_1 = float(input("Enter first number: "))

        num_2 = float(input("Enter second number: "))

        to_do = input('What do you want to do? Add this numbers "+", substract "-", multiple "*", divide "/", pow "**" ')

        result = float()

        if to_do == '+':
            result =  to_sum(num_1, num_2)
        elif to_do == '-':
            result = to_substract(num_1, num_2)
        elif to_do == '*':
            result = to_multiple(num_1, num_2)
        elif to_do == '/':
            if num_2 != 0:
                result = to_divide(num_1, num_2)
            else:
                print('You cannot divide to zero')
        elif to_do == '**':
            result = to_pow(num_1, num_2)


        print(result)

        with open(file_path, 'a') as calc:
            calc.write(f"{num_1}{to_do}{num_2} = {result}")

    except Exception as e:
        print(f'There is an error: {e}')

if __name__ == '__main__':
    result_path = 'result.txt'
    save_result(result_path)