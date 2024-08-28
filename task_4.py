from fractions import Fraction

def process_fractions(fraction1, fraction2):
    # Преобразуем строку в объекты
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)
 
    # Считаем сумму и произведение
    sum_result = frac1 + frac2
    product_result = frac1 * frac2

    return sum_result, product_result

# Пример использования
fraction1 = "1/2"
fraction2 = "3/4"

sum_result, product_result = process_fractions(fraction1, fraction2)

print(f"Сумма: {sum_result}")
print(f"Произведение: {product_result}")