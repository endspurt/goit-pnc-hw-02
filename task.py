def vigenere_encrypt(text, key):
    """
    Шифрує текст за допомогою шифру Віженера
    """
    encrypted = []
    key = key.upper()
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Конвертуємо літери в числа (A=0, B=1, і т.д.)
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            # Обчислюємо зашифровану літеру
            shift = ord(key[key_index % key_length]) - ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            
            key_index += 1
            encrypted.append(encrypted_char)
        else:
            # Зберігаємо не-алфавітні символи без змін
            encrypted.append(char)
    
    return ''.join(encrypted)

def vigenere_decrypt(encrypted_text, key):
    """
    Розшифровує текст, зашифрований шифром Віженера
    """
    decrypted = []
    key = key.upper()
    key_length = len(key)
    key_index = 0
    
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            # Обчислюємо розшифровану літеру
            shift = ord(key[key_index % key_length]) - ord('A')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            
            key_index += 1
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)

def simple_columnar_transposition_encrypt(text, key):
    """
    Шифрує текст за допомогою простої перестановки стовпців
    """
    # Видаляємо пробіли та конвертуємо у верхній регістр
    text = ''.join(filter(str.isalnum, text.upper()))
    
    # Створюємо матрицю
    key_length = len(key)
    if len(text) % key_length != 0:
        text += 'X' * (key_length - (len(text) % key_length))
    
    # Заповнюємо матрицю
    num_rows = len(text) // key_length
    matrix = [[''] * key_length for _ in range(num_rows)]
    
    for i, char in enumerate(text):
        row = i // key_length
        col = i % key_length
        matrix[row][col] = char
    
    # Створюємо порядок стовпців на основі ключа
    key_order = sorted(range(key_length), key=lambda k: key[k])
    
    # Читаємо стовпці у правильному порядку
    encrypted = ''
    for col in key_order:
        for row in range(num_rows):
            encrypted += matrix[row][col]
    
    return encrypted

def simple_columnar_transposition_decrypt(encrypted_text, key):
    """
    Розшифровує текст, зашифрований простою перестановкою стовпців
    """
    key_length = len(key)
    num_rows = len(encrypted_text) // key_length
    
    # Створюємо зворотній порядок ключа
    key_order = sorted(range(key_length), key=lambda k: key[k])
    inverse_key = [0] * key_length
    for i, k in enumerate(key_order):
        inverse_key[k] = i
    
    # Створюємо та заповнюємо матрицю
    matrix = [[''] * key_length for _ in range(num_rows)]
    pos = 0
    
    for col in key_order:
        for row in range(num_rows):
            matrix[row][col] = encrypted_text[pos]
            pos += 1
    
    # Читаємо матрицю по рядках
    decrypted = ''
    for row in range(num_rows):
        for col in range(key_length):
            decrypted += matrix[row][col]
    
    return decrypted

# Приклад використання
text = """The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim."""
key_vigenere = "CRYPTOGRAPHY"
key_transposition = "SECRET"

# Тестуємо шифр Віженера
encrypted_vigenere = vigenere_encrypt(text, key_vigenere)
decrypted_vigenere = vigenere_decrypt(encrypted_vigenere, key_vigenere)

# Тестуємо перестановку
encrypted_trans = simple_columnar_transposition_encrypt(text, key_transposition)
decrypted_trans = simple_columnar_transposition_decrypt(encrypted_trans, key_transposition)

# Виводимо результати
print("Оригінальний текст:", text)
print("\nШифр Віженера:")
print("Зашифрований текст:", encrypted_vigenere)
print("Розшифрований текст:", decrypted_vigenere)
print("\nШифр перестановки:")
print("Зашифрований текст:", encrypted_trans)
print("Розшифрований текст:", decrypted_trans)