def fsa_plural_noun(word):
  INITIAL = 0
  VOWEL = 1
  CONSONANT = 2
  Y_AFTER_VOWEL = 3
  YS_AFTER_VOWEL = 4
  I_AFTER_CONSONANT = 5
  IE_AFTER_CONSONANT = 6
  IES_AFTER_CONSONANT = 7
  
  STATE = INITIAL
  
  for w in word:
    if STATE == INITIAL:
      if w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
    elif STATE == VOWEL:
      if w == "y":
        STATE = Y_AFTER_VOWEL
      elif w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
    elif STATE == CONSONANT:
      if w == "i":
        STATE = I_AFTER_CONSONANT
      elif w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
    elif STATE == Y_AFTER_VOWEL:
      if w == "s":
        STATE = YS_AFTER_VOWEL
      elif w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
    elif STATE == I_AFTER_CONSONANT:
      if w == "e":
        STATE = IE_AFTER_CONSONANT
      elif w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
    elif STATE == IE_AFTER_CONSONANT:
      if w == "s":
        STATE = IES_AFTER_CONSONANT
      elif w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
    elif STATE == YS_AFTER_VOWEL:
      if w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
    elif STATE == IES_AFTER_CONSONANT:
      if w in "aeiou":
        STATE = VOWEL
      else:
        STATE = CONSONANT
  
  if STATE in (YS_AFTER_VOWEL, IES_AFTER_CONSONANT):
    return True
  return False

test_words = ["boys", "toys", "ponies", "skies", "puppies", "boies", "toies", "ponys"]
results = {word: fsa_plural_noun(word) for word in test_words}
print(results)