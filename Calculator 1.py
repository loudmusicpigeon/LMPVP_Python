num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))
op = input('Enter an operation (+ - * /). ')
if op=='+':
    result = (num1) + (num2)
    print(num1, '+', num2, '=', result)
elif op=='-':
    if num1>num2:
        result = (num1) - (num2)
        print(num1, '-', num2, '=', result)
    else:
        result = (num2) - (num1)
        print(num2, '-', num1, '=', result)
elif op=='*':
    result = (num1) * (num2)
    print(num1, '×', num2, '=', result)
elif op=='/':
    if num1>num2:
        result = (num1) / (num2)
        print(num1, '÷', num2, '=', result)
    else:
        result = (num2) / (num1)
        print(num2, '÷', num1, '=', result)
else:
    print('Invalid operation')