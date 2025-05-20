def number_to_words(num):
    digits = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join(digits[d] for d in num)


def process_file(text):
    with open(text, 'r') as file:
        content = file.read()

    words = content.split()
    numbers_found = []

    for word in words:
        if word.startswith('202') and '.' in word:
            num_part = word.replace('.', '', 1)
            if num_part.isdigit():
                if int(num_part) % 2 != 0:
                    processed_num = word.replace('.', ',')
                    numbers_found.append(processed_num)

    if numbers_found:
        print("Первое число прописью:")
        first_num = numbers_found[0].replace(',', '.')
        digits_only = [c for c in first_num if c.isdigit()]
        print(number_to_words(digits_only))

        print("\nВсе подходящие числа:")
        for num in numbers_found:
            print(num)
    else:
        print("Подходящих чисел не найдено.")

process_file(r'C:\Users\UserPC\Desktop\text\text.txt')
