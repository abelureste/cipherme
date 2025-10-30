def gematria():
  print("\n----- You've chosen to use an English Gematria Cipher -----")
  string = input("Enter the message you would like to encode: \n")

  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  key = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156]

  def encode(string):
    string = list(string)
    encoded_string = []

    for char in string:
      if char in alphabet:
        position = alphabet.index(char)
      encoded_string.append(key[position])
    
    return encoded_string
  
  encoded_array = encode(string)

  print(f"Your encoded message is: {(sum(encoded_array))}")