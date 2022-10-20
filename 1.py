def translation(number_func, numeral_sys_func):
    integer_part = int(number_func)
    fractional_part = float("0." + str(number_func)[str(number_func).index(".")+1:])
    if integer_part == 0:
        new_integer_part = '0'
    else:
        new_integer_part = ''
        while integer_part:
            new_integer_part = str(integer_part % numeral_sys_func) + new_integer_part
            integer_part //= numeral_sys_func
    if int(number_func) == number_func:
        return new_integer_part
    else:
        new_fractional_part = ''
        fractional_part_of_result = fractional_part
        result = fractional_part
        accuracy = 0      #так как может получиться, что дробь будет бесконечной, необходимо ввести точность (пусть будет 16 знаков после запятой)
        while fractional_part_of_result != 0 and accuracy != 16:
            result = result * numeral_sys_func
            integer_part_of_result = int(result) % numeral_sys_func
            fractional_part_of_result = result - int(result)
            new_fractional_part += str(integer_part_of_result)
            accuracy += 1
        return new_integer_part + "." + new_fractional_part


number = float(input("Введите число для перевода: "))
while True:
    numeral_system = int(input("Введите в какую систему счисления перевести число(в 2-ную или 8-ную): "))
    if numeral_system != 2 and numeral_system != 8:
        print("Некорректный ввод системы счисления! Повторите попытку.")
    else:
        break
print("Результат перевода:", translation(number, numeral_system))