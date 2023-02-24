romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
num = input('Ingresar el numero romano: ')

def romano_a_decimal(number):
    decimal = []
    romano = 0
    for i in number:
        decimal.append(romanos[i])
    romano = decimal[-1]

    for digit in reversed(range(len(decimal))):
        if digit == 0:
            break
        if decimal[digit] > decimal[digit-1]:
            romano -= decimal[digit-1]
        else:
            romano += decimal[digit-1]
        
    return romano
if romano_a_decimal(num) > 3999: #esto es pq los numeros romanos no superan los 4mil en teclado
    raise ValueError
print(num, 'es igual a:', romano_a_decimal(num))
