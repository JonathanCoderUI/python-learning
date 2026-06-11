number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

pilihan = input("Choose an operation (+, -, *, /, **): ")
if pilihan == '+':
    hasil = number1 + number2
    print("Result:", hasil)
elif pilihan == '-':
    hasil = number1 - number2
    print("Result:", hasil)
elif pilihan == '*':
    hasil = number1 * number2
    print("Result:", hasil)
elif pilihan == '/':
    if number2 != 0:
        hasil = number1 / number2
        print("Result:", hasil)
    else:
        print("Error: Division by zero is not allowed.")
elif pilihan == '**':
    hasil = number1 ** number2
    print("Result:", hasil)
else:
    print("Invalid operation selected.")