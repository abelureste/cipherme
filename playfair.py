def playfair():
  print("\n----- You've chosen to use a Playfair Cipher -----")
  key = input("Enter the key you would like to use: \n").lower()
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  def generate_tableau(key):
    key = list(key)
    tableau_values = []
    
    tableau = [[0 for x in range(5)] for y in range(5)]


    for char in key:
      if char in alphabet and char not in tableau_values:
        tableau_values.append(char)

    for char in alphabet:
      if char == 'j':
        continue
      if char not in tableau_values:
        tableau_values.append(char)

    count = 0

    for i in range(len(tableau)):
      for j in range(len(tableau[i])):
        tableau[i][j] = tableau_values[count]
        count += 1

    return tableau
  
  tableau = generate_tableau(key)
  
  def print_tableau(array2d):
    print("Your encoding tableau is: ")
    for row in array2d:
      print(' '.join(row))

  print_tableau(tableau)

  string = input("Enter the word you would like to encode: \n")

  def process_string(string):
    string = str(string)
    string = string.lower().replace('j','i')

    digraphs = []
    i = 0
    while i < len(string):

      if i == len(string) - 1:
        digraphs.append(string[i] + 'x')
        i += 1
      elif string[i] == string[i + 1]:
        digraphs.append(string[i] + 'x')
        i += 1
      else:
        digraphs.append(string[i] + string[i + 1])
        i += 2

    return digraphs

  digraphs = process_string(string)

  def find_char_coords(char ,tableau):
    for i in range(5):
      for j in range(5):
        if tableau[i][j] == char:
          return[j, i]
    return (None, None)
        
  def encode(digraphs, tableau):
    encoded_pairs = []

    for pair in digraphs:
      char1 = pair[0]
      char2 = pair[1]

      (r1, c1) = find_char_coords(char1, tableau)
      (r2, c2) = find_char_coords(char2, tableau)

      if r1 is None or r2 is None:
        continue 

      if r1 == r2:
        encoded_pairs.append(tableau[r1][(c1 + 1) % 5])
        encoded_pairs.append(tableau[r2][(c2 + 1) % 5])
        
      elif c1 == c2:
        encoded_pairs.append(tableau[(r1 + 1) % 5][c1])
        encoded_pairs.append(tableau[(r2 + 1) % 5][c2])
        
      else:
        encoded_pairs.append(tableau[c1][r2])
        encoded_pairs.append(tableau[c2][r1]) 

    return ''.join(encoded_pairs)

  print(f'Youre encoded message is: \n{encode(digraphs, tableau)}')