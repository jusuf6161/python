from replit import clear

kelimeler = ["python", "zurna", "roman", "tavuk", "yusuf", "çakır", "of"]
stages = [
  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
import random

word = random.choice(kelimeler)

len = len(word)

lives = 6
display = []
for letters in range(len):
  display += '_'

oyun_sonu = False
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
while oyun_sonu == False:
  guess = input("Harf Tahmin Edin: ").lower()
  clear()
  for position in range(len):
    letter = word[position]

    if letter == guess:
      display[position] = letter
  if guess not in word:
    print(
      f"Sectiğin Harf {guess}, Kelimenin İçinde Malesef Yok . Canını Kaybettin"
    )
    lives -= 1
    if lives == 0:
      oyun_sonu = True
      print("Malesef Kaybettin Terar Dene ! ")

  print(display)
  if not '_' in display:
    oyun_sonu = True
    print("Kazandın Tebrikler!! ")

  print(stages[lives])
