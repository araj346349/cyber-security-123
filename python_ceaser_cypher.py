def encrypt(text, shift):
  """Encrypts a text using the Caesar cipher with a given shift."""
  encrypted_text = ""
  for char in text:
    if char.isalpha():  # Encrypt only alphabetic characters
      shift_amount = shift % 26  # Handle shifts greater than 26
      char_code = ord(char)
      if char.islower():
        encrypted_char = chr(((char_code - ord('a') + shift_amount) % 26) + ord('a'))
      else:
        encrypted_char = chr(((char_code - ord('A') + shift_amount) % 26) + ord('A'))
    else:
      encrypted_char = char  # Keep non-alphabetic characters as is
    encrypted_text += encrypted_char
  return encrypted_text

def decrypt(text, shift):
  """Decrypts a text encrypted with the Caesar cipher."""
  return encrypt(text, -shift)  # Decrypting is just encrypting with the opposite shift

# Get user input
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

# Encrypt and decrypt
encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)