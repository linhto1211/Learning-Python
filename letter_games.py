letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Score a word
letter_to_points={key:value for key, value in zip(letters,points)}
letter_to_points.update({" ":0})
print(letter_to_points)
def score_word(word):
  point_total=0
  for w in word:
    for index in list(range(len(letters))):
      if w == letters[index]:
        point_total+=letter_to_points.get(letters[index])
    else:
      point_total+=0
  return point_total

brownie_points=score_word("BROWNIE")
print(brownie_points)

#Score a game
player_to_words={"player1": ["BLUE","TENNIS","EXIT"],"wordNerd": ["EARTH","EYES","MACHINE"], "Lexi Con": ["ERASER","BELLY","HUSKY"], "Prof Reader": ["ZAP","COMA","PERIOD"]}
print(player_to_words.items())
player_to_points={}
for player, words in player_to_words.items():
    player_points=0
    for wo in words:
      player_points+=score_word(wo)
      print(wo)
    print(player_points)
    player_to_points[player]=player_points
  


