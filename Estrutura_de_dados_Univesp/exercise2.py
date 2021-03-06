def next_letter ():
  word = input ("Write a word: ")
  word_to_list = list(word)
  next_letter_word = ""
  for letter in word_to_list:
    if (letter == "z"): next_letter_word += "a"   
    elif (letter == "Z"): next_letter_word += "A"
    else: next_letter_word += chr(ord(letter) + 1)
  print (next_letter_word)
