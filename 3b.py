import random
deck=["Diamonds","Spades","Hearts","Clubs"]
print("Before Shuffling: ", deck)
random.shuffle(deck)
print("After Shuffling", deck)
print("Randomly drawing a suit: " , random.choice(deck))
New_deck=random.sample(deck,2)
print("New Deck: ",New_deck)