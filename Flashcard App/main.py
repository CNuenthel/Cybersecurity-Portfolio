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
                 "ipv4PacketFields\n"
                 "ipv6PacketFields\n"
                 "wireshark\n"
                 "logs\n"
                 "osiModel\n"
                 "\n"
                 "Type quit to end\n")


while True:
    while True:
        result = request_decktype()

        match result:
            case "Bash":
                pass

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
