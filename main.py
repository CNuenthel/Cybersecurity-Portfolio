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
                 "Threat Model\n"
                 "Intrusion and Detection\n"
                 "NIST\n"
                 "\n"
                 "Type quit to end\n")


while True:
    while True:
        result = request_decktype()

        match result:
            case "Bash":
                print("You chose Bash!\n")
                deck = flashcards.FlashcardDeck(flashcards.bashCards)
                break

            case "SQL":
                print("You chose SQL!\n")
                deck = flashcards.FlashcardDeck(flashcards.sqlCards)
                break

            case "Resource":
                print("You chose Resource!\n")
                deck = flashcards.FlashcardDeck(flashcards.resourceCards)
                break

            case "Threat Model":
                print("You chose Threat Model!\n")
                deck = flashcards.FlashcardDeck(flashcards.threatModel)
                break

            case "Alert and Event Management":
                print("You chose Intrusion and Detection!\n")
                deck = flashcards.FlashcardDeck(flashcards.alertAndEventManagement)
                break

            case "NIST":
                print("You chose NIST!\n")
                deck = flashcards.FlashcardDeck(flashcards.NIST)
                break

            case "Quit":
                print("Bye!")
                exit()

    print(f"There are {len(deck.card_dictionary)} cards in this deck!\n")

    while True:
        card = deck.deal_card()

        if card:
            input(f"{card.face}")
            input(f"{card.definition}\n")

        else:
            print("Thats all of the cards! Well done!")
            break
