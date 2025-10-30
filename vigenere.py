def vigenere():
  print("\n----- You've chosen to use a Vigenere Cipher -----")
  string = input("Enter the message you would like to encode: \n").lower()
  key = input("Enter the key you would like to use: \n").lower()
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  string = list(string)
  key = list(key)

  def calc_keystream():
    keystream = []

    if len(key) < len(string):
      index = 0

      for i in range(len(string)):
        if string[i] == ' ':
          keystream.append(' ')
          continue

        try:
          keystream.append(key[index])
          index += 1
        except IndexError:
          index = 0
          keystream.append(key[index])
          index += 1

    else:
      for i in range(len(string)):
        keystream.append(key[i])

    return keystream
  
  keystream = calc_keystream()
  print(f"Your keystream is: \n{"".join(keystream)}")

  def create_matrix():
    vigenere_matrix = []    

    for i in range(len(alphabet)):
      row = alphabet[i:] + alphabet[:i]
      vigenere_matrix.append(list(row))

    return vigenere_matrix
  
  vigenere_matrix = create_matrix()

  def encode(string):
    s_coordinates = []
    k_coordinates = []
    final_message = []

    for char in string:
      if char in alphabet:
        s_coordinates.append(alphabet.index(char))
      elif char == ' ':
        s_coordinates.append(' ')
    for char in keystream:
      if char in alphabet:
        k_coordinates.append(alphabet.index(char))
      elif char == ' ':
        k_coordinates.append(' ')

    for i in range(len(s_coordinates)):
      if (s_coordinates[i] == ' ' and k_coordinates[i] == ' '):
        final_message.append(' ')
        continue
      value = vigenere_matrix[s_coordinates[i]][k_coordinates[i]]
      final_message.append(value)
 
    return "".join(final_message)

  print(f"Your encoded message is: \n{encode(string)}")