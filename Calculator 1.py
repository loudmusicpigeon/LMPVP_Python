num1 = input('Enter a number: ')
num2 = input('Enter a number: ')
op = input('Enter an operation (+ - * /). ')
if op=='+':
    result = float(num1) + float(num2)
    print(num1, '+', num2, '=', result)
elif op=='-':
    if num1>num2:
        result = float(num1) - float(num2)
        print(num1, '-', num2, '=', result)
    else:
        result = float(num2) - float(num1)
        print(num2, '-', num1, '=', result)
elif op=='*':
    result = float(num1) * float(num2)
    print(num1, '×', num2, '=', result)
elif op=='/':
    if num1>num2:
        result = float(num1) / float(num2)
        print(num1, '÷', num2, '=', result)
    else:
        result = float(num2) / float(num1)
        print(num2, '÷', num1, '=', result)
else:
    print('Invalid operation')