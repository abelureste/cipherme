from logo import logo
from caesar_cipher import caesar_cipher
from atbash import atbash
from gematria import gematria

cipher_name_list = "1 : Caesar Cipher \n 2 : Atbash Cipher \n 3 : English Gematria \n 4 : Vigenere Cipher \n 5 : Playfair Cipher \n 6 : Columnar Transposition Cipher \n 7 : Baconian Cipher"
cipher_list = {
  '1' : caesar_cipher,
  '2' : atbash,
  '3' : gematria,
  }

print(logo)
print(f"----- Supported Ciphers ----- \n {cipher_name_list} \n")
chosen_cipher = input("Which cipher would you like to use? (Enter number): \n")

if chosen_cipher in cipher_list:
  cipher_list[chosen_cipher]()
else:
  print("Cipher was not found in list.")