def gematria():
  print("\n----- You've chosen to use an English Gematria Cipher -----")
  string = input("Enter the message you would like to encode: \n").lower()

  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  key = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156]

  def encode(string):
    string = list(string)
    encoded_string = []
    result_array = []

    for char in string:
      if char in alphabet:
        position = alphabet.index(char)
        encoded_string.append(key[position])
      if char == ' ':
        result_array.append(sum(encoded_string))
        encoded_string = []
      if char == string[-1]:
        result_array.append(sum(encoded_string))      

    return result_array
  
  result = encode(string)

  if len(result) > 1:
    result_sum = sum(result)
    result = " ".join(map(str, result))
    print(f"Your words are encoded to: \n{result}")
    print(f"Your final encoded message is: \n{result_sum}")
  else:
    result = " ".join(map(str, result))
    print(f"Your encoded message is: \n{result}")