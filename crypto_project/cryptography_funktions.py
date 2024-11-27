# Датотека: cryptography_functions.py

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
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            shift = ord(key[key_index % key_length]) - ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            
            key_index += 1
            encrypted.append(encrypted_char)
        else:
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
    text = ''.join(filter(str.isalnum, text.upper()))
    
    key_length = len(key)
    if len(text) % key_length != 0:
        text += 'X' * (key_length - (len(text) % key_length))
    
    num_rows = len(text) // key_length
    matrix = [[''] * key_length for _ in range(num_rows)]
    
    for i, char in enumerate(text):
        row = i // key_length
        col = i % key_length
        matrix[row][col] = char
    
    key_order = sorted(range(key_length), key=lambda k: key[k])
    
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
    
    key_order = sorted(range(key_length), key=lambda k: key[k])
    inverse_key = [0] * key_length
    for i, k in enumerate(key_order):
        inverse_key[k] = i
    
    matrix = [[''] * key_length for _ in range(num_rows)]
    pos = 0
    
    for col in key_order:
        for row in range(num_rows):
            matrix[row][col] = encrypted_text[pos]
            pos += 1
    
    decrypted = ''
    for row in range(num_rows):
        for col in range(key_length):
            decrypted += matrix[row][col]
    
    return decrypted

# Датотека: input.txt
"""
The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless.
"""