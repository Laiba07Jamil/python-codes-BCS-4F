total_cards = 52

red_cards = 26

hearts = 13

face_cards = 12

diamond_face_cards = 3

spade_face_cards = 3

queens = 4

spade_queen = 1

prob_red = red_cards / total_cards

prob_heart_given_red = hearts / red_cards

prob_diamond_given_face = diamond_face_cards / face_cards

prob_spade_or_queen_given_face = (spade_face_cards + queens - spade_queen) / face_cards

print("Probability of drawing a red card:", prob_red)
print("Probability of heart given red card:", prob_heart_given_red)
print("Probability of diamond given face card:", prob_diamond_given_face)
print("Probability of spade or queen given face card:", prob_spade_or_queen_given_face)