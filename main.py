import copy
import random

import flashcards

# Welcome
print("Welcome to Cody's text based flashcard system \n")


# Collect flashcard database input
def request_decktype():
    return input("Which deck of flashcards would you like to go through? \n"
                 "Bash\n"
                 "SQL\n"
                 "Resource\n"
                 "\n"
                 "Type quit to end\n")


while True:
    while True:
        result = request_decktype()

        if result.title() == "Bash":
            print("You chose Bash!\n")
            deck = flashcards.FlashcardDeck(flashcards.bashCards)
            break

        elif result.upper() == "SQL":
            print("You chose SQL!\n")
            deck = flashcards.FlashcardDeck(flashcards.sqlCards)
            break

        elif result.title() == "Resource":
            print("You chose Resource!\n")
            deck = flashcards.FlashcardDeck(flashcards.resourceCards)
            break

        elif result.title() == "Quit":
            print("Bye!")
            exit()

        else:
            print("I'm sorry, I didn't quite understand that, please type a number to select.")
            request_decktype()

    print(f"There are {len(deck.card_dictionary)} cards in this deck!\n")

    while True:
        card = deck.deal_card()

        if card:
            input(f"{card.face}")
            input(f"{card.definition}\n")

        else:
            print("Thats all of the cards! Well done!")
            break
