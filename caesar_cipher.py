def caesar_cipher():
  print("\n----- You've chosen to use a Caesar Cipher -----")
  string = input("Enter the message you would like to encode: \n").lower()
  shift = int(input("Enter a shift value: \n"))

  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  def shiftKey(array, shift_amount):
    shift_amount = shift_amount % len(array)
    return array[shift_amount:] + array[:shift_amount]

  key = shiftKey(alphabet, shift)

  def encode(string):
    string = list(string)
    encoded_string = []

    for char in string:
      if char in alphabet:
        position = alphabet.index(char)
        char = key[position]
        encoded_string.append(char)
      if char == ' ':
        encoded_string.append(' ')

    return "".join(encoded_string)
  
  print(f"Your encoded message is: \n{encode(string)}")