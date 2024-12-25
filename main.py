import math

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# Функция поточного шифрования
def stream_cipher(text, shift, alphabet):
   encrypted_text = ""
   for char in text:
       if char in alphabet:
           index = alphabet.index(char)
           new_index = (index + shift) % len(alphabet)
           encrypted_text += alphabet[new_index]
       else:
           encrypted_text += char 
   return encrypted_text

# Функция перестановки столбцов
def columnar_transposition(text, keyword):
   # Удалим повторяющиеся символы в ключевом слове
   keyword = "".join(sorted(set(keyword), key=keyword.index))
   # Считаем количество столбцов
   num_columns = len(keyword)
   # Разбиваем текст на строки с количеством символов, равным длине ключевого слова
   rows = [text[i:i + num_columns] for i in range(0, len(text), num_columns)]
   # Заполняем последнюю строку пробелами, если она короче
   if len(rows[-1]) < num_columns:
       rows[-1] += ' ' * (num_columns - len(rows[-1]))
   # Сортируем столбцы по алфавитному порядку ключевого слова
   sorted_keyword = sorted(list(keyword))
   # Формируем зашифрованный текст путем перестановки столбцов
   encrypted_text = ""
   for letter in sorted_keyword:
       col_index = keyword.index(letter)
       for row in rows:
           if col_index < len(row):
               encrypted_text += row[col_index]
   return encrypted_text

# Преобразуем открытый текст
def preprocess_text(text):
   replacements = {
       ",": "ЗПТ", ".": "ТЧК", "!": "ВСКЗН", "?": "ВПСЗН",
       ";": "ТЧКЗП", ":": "ДВТЧ", "–": "ТИРЕ"
   }
   for old, new in replacements.items():
       text = text.replace(old, new)
   return text.replace(' ', '').upper()

# Входные данные
plaintext = "О капитан! Мой капитан! Рейс трудный завершён, все бури выдержал корабль, увенчан славой он..."
shift = 8
keyword = "ЯКОРЬ"

# Шаг 1: Преобразуем открытый текст
processed_text = preprocess_text(plaintext)
print("Преобразованный текст:", processed_text)

# Шаг 2: Применяем поточное шифрование
encrypted_text = stream_cipher(processed_text, shift, alphabet)
print("Зашифрованный текст:", encrypted_text)

# Шаг 3: Применяем перестановку по ключу
final_encrypted_text = columnar_transposition(encrypted_text, keyword)
print("Текст после перестановки:", final_encrypted_text)