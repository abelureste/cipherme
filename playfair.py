def playfair():
  print("\n----- You've chosen to use an English Gematria Cipher -----")
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
    for i in array2d:
      print('')
      for j in i:
        print(j, end=' ')
    print('\n')

  print_tableau(tableau)

  string = input("Enter the word you would like to encode: \n").lower()


playfair()