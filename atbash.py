def atbash():
  print("\n----- You've chosen to use an Atbash Cipher -----")
  string = input("Enter the message you would like to encode: \n")

  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  key = list(reversed(alphabet))

  def encode(string):
    string = list(string)
    encoded_string = []

    for char in string:
      if char in alphabet:
        position = alphabet.index(char)
      char = key[position]
      encoded_string.append(char)

    return "".join(encoded_string)

  print(f"Your encoded message is: \n{encode(string)}")