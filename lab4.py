import re


def number_to_words(number):
    digit_words = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять',
        '.': 'точка',
        ',': 'запятая',
        '-': 'минус'
    }
    return ' '.join(digit_words[digit] for digit in str(number))


def process_file(text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'\b202\d*\.\d+\b'
    numbers = re.findall(pattern, content)

    odd_numbers = []
    for num in numbers:
        if int(num.replace('.', '')[3:]) % 2 != 0:
            odd_numbers.append(num)

    if not odd_numbers:
        print("Не найдено подходящих чисел.")
        return

    first_num = odd_numbers[0]
    first_num_words = number_to_words(first_num)
    print(f"Первое число прописью: {first_num_words}")

    print("\nВсе подходящие числа:")
    for num in odd_numbers:
        converted_num = num.replace('.', ',')
        print(converted_num)

process_file(r'C:\Users\UserPC\Desktop\input\input.txt')