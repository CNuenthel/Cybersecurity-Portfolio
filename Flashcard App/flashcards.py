import json


# Define the flashcard model
class Flashcard:
    def __init__(self, face: str, definition: str):
        self.face = face
        self.definition = definition


class FlashcardDeck:
    def __init__(self, card_dictionary: dict):
        self.card_database = None
        self.card_dictionary = card_dictionary
        self._create_db()

    def _create_db(self):
        with open("flashcards.json", "r") as f:
            self.card_database = json.load(f)

    def load_subsection(self, subsection_name: str) -> dict:
        self.card_dictionary = self.card_database[subsection_name]
        return self.card_dictionary

    def deal_card(self) -> Flashcard or bool:
        # Creates a flashcard and returns it if card data is available from given dictionary
        try:
            # Get card data from given dictionary
            card_face, card_definition = self.card_dictionary.popitem()

            # Make flashcard
            return Flashcard(card_face, card_definition)

        except KeyError:  # Return False if dictionary is empty and flash cards have run out
            return False

    def cycle_card(self, card: Flashcard):
        # Return a card to the deck
        self.card_dictionary[card.face] = card.definition


