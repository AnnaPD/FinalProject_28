from random import choice
from string import ascii_uppercase
import random
import string



valid_email_auth = 'Email@mail.ru'
valid_password_auth = '123Abc12'
valid_phone_auth = '89276880123'
valid_personal_account_auth = '363020399123'
valid_firstname = 'Семён'
valid_lastname = 'Шлепаков'
valid_email_reg = 'AnnaDePe+2@yandex.ru'
valid_phone_reg = '+78462269123'
valid_password_reg = '123Abc001'
valid_password_reg_repeat = '123Abc001'
invalid_email_reg = 'Email@mail.ru'
invalid_phone_reg = '89276880123'
invalid_pass_repeat = '123Abc03'



# генерация строки из случайных символов в нижнем регистре
def generation_lower_string(length):
    result = ''.join(
        (random.choice(string.ascii_lowercase) for x in range(length)))
    print(result)
    return result

generation_lower_string(5)


# генерация строки из случайных символов в верхнем регистре
def generation_upper_string(length):
    result = ''.join(
        (random.choice(string.ascii_uppercase) for x in range(length)))
    print(result)
    return result
generation_upper_string(8)


# генерация строки из случайных символов из прописных и строчных букв
def generation_letters_string(length):
    result = ''.join(
        (random.choice(string.ascii_letters) for x in range(length)))
    print(result)
    return result
generation_letters_string(10)


# генерация цифровой строки
def generation_digits_string(digit_count):
    result = ''.join(
        (random.choice(string.digits) for x in range(digit_count)))
    print(result)
    return result
generation_digits_string(10)


# генерация строки с символами пунктуации
def generation_punctuation_string(length):
    result = ''.join(
        (random.choice(string.punctuation) for x in range(length)))
    print(result)
    return result
generation_punctuation_string(10)


# генерация буквенно-цифровой строки
def generation_random_string(letter_count, digit_count):
    str = ''.join(
        (random.choice(string.ascii_letters) for x in range(letter_count)))
    str += ''.join(
        (random.choice(string.digits) for x in range(digit_count)))

    sam_list = list(str)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    print(final_string)
    return final_string
generation_random_string(5, 3)


# генерация строки из случайных символов на кририллице
def generation_specific_string_сyrillic(length):
    sample_string = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
    result = ''.join((random.choice(sample_string)) for x in range(length))
    print(result)
    return result
generation_specific_string_сyrillic(12)


# генерация строки из случайных китайских иероглифов
def generation_specific_string_сhinese_char(length):
    sample_string = '的一了是我不在人们有回家晚上美学习国'
    result = ''.join((random.choice(sample_string)) for x in range(length))
    print(result)
    return result
generation_specific_string_сhinese_char(12)
