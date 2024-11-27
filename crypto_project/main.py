# Датотека: main.py

import os
from cryptography_functions import (
    vigenere_encrypt,
    vigenere_decrypt,
    simple_columnar_transposition_encrypt,
    simple_columnar_transposition_decrypt
)

def read_text_file(filename):
    """Читає текст з файлу"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_text_file(filename, text):
    """Записує текст у файл"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    # Зчитуємо вхідний текст
    input_text = read_text_file('input.txt')
    
    # Ключі для шифрування
    key_vigenere = "CRYPTOGRAPHY"
    key_transposition = "SECRET"
    
    # Шифр Віженера
    encrypted_vigenere = vigenere_encrypt(input_text, key_vigenere)
    write_text_file('encrypted_vigenere.txt', encrypted_vigenere)
    
    # Перевірка розшифрування Віженера
    decrypted_vigenere = vigenere_decrypt(encrypted_vigenere, key_vigenere)
    write_text_file('decrypted_vigenere.txt', decrypted_vigenere)
    
    # Шифр перестановки
    encrypted_trans = simple_columnar_transposition_encrypt(input_text, key_transposition)
    write_text_file('encrypted_transposition.txt', encrypted_trans)
    
    # Перевірка розшифрування перестановки
    decrypted_trans = simple_columnar_transposition_decrypt(encrypted_trans, key_transposition)
    write_text_file('decrypted_transposition.txt', decrypted_trans)
    
    # Комбінований шифр (Віженер + перестановка)
    combined_encryption = simple_columnar_transposition_encrypt(
        vigenere_encrypt(input_text, key_vigenere),
        key_transposition
    )
    write_text_file('encrypted_combined.txt', combined_encryption)
    
    print("Шифрування завершено. Перевірте файли з результатами.")

if __name__ == "__main__":
    main()

