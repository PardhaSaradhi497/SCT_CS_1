Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Simple Caesar Cipher in Python
... 
... def encrypt(text, shift):
...     result = ""
...     for char in text:
...         if char.isalpha():  # only letters
...             base = ord('A') if char.isupper() else ord('a')
...             result += chr((ord(char) - base + shift) % 26 + base)
...         else:
...             result += char  # keep spaces, numbers, symbols same
...     return result
... 
... def decrypt(text, shift):
...     return encrypt(text, -shift)
... 
... # Main program
... message = input("Enter your message: ")
... shift = int(input("Enter shift value: "))
... 
... encrypted = encrypt(message, shift)
... print("Encrypted message:", encrypted)
... 
... decrypted = decrypt(encrypted, shift)
