from logo import logo
from caesar_cipher import caesar_cipher
from atbash import atbash
from gematria import gematria
from vigenere import vigenere
from playfair import playfair

cipher_name_list = "1 : Atbash Cipher  \n 2 : Caesar Cipher \n 3 : English Gematria Cipher \n 4 : Vigenere Cipher \n 5 : Playfair Cipher \n 6 : Columnar Transposition Cipher \n 7 : Baconian Cipher"
cipher_list = {
  '1' : atbash,
  '2' : caesar_cipher,
  '3' : gematria,
  '4' : vigenere,
  '5' : playfair,
  }

print(logo)
print("----- Information -----")
print("This program only supports the standard 26 letter English alphabet from A - Z.")
print("To use this program, choose a cipher then input any English word or sentence. \n")
print(f"----- Supported Ciphers ----- \n {cipher_name_list} \n")
chosen_cipher = input("Which cipher would you like to use? (Enter number): \n")

if chosen_cipher in cipher_list:
  cipher_list[chosen_cipher]()
else:
  print("Cipher was not found in list.")