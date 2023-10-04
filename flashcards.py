
# Define the flashcard model
class Flashcard:
    def __init__(self, face: str, definition: str):
        self.face = face
        self.definition = definition


class FlashcardDeck:
    def __init__(self, card_dictionary: dict):
        self.card_dictionary = card_dictionary

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


sqlCards = {
    "inner join": "returns rows matching on a specified column that exists in more than one table.",
    "outer join": "Outer joins expand what is returned from a join. Each type of outer join returns all rows from "
                  "either one table or both tables",
    "full outer join": "returns all records from both tables",
    "left join": "returns all the records of the first table, but only returns rows of the second table that "
                       "match on a specified column",
    "right join": "returns all of the records of the second table, but only returns rows from the first table that "
                  "match on a specified column",
    "select": "indicates which columns to return",
    "where": "indicates the condition of a filter",
    "count": "returns a single number that represents the number of rows returned from your query i.e. SELECT COUNT(firstname) FROM tablename",
    "avg": "returns a single number that represents the average of the numerical data in a column",
    "sum": "returns a single number that represents the sum of the numerical data in a column",
    "from": "indicates which table to query",
    "order by": "sequences the requested data by the given column or columns",
    "between": "filters for numbers or dates within a range",
    "and": "specifies both given conditions must be met",
    "like": "used with  WHERE to search for a pattern in a column, i.e. [WHERE title LIKE 'IT%']",
    "not": "negates a condition, returns information not matching given criteria",
    "or": "specifies either given condition must be met",
    "%": "wildcard pattern with LIKE, indicates variable number of possible characters",
    "_": "wildcard pattern with LIKE, indicates a single additional variable character",
    "sqlinjection categories": "in-band, out-of-band, inferential",
    "in-band": "sql query code injected in an input that returns the result in the used input",
    "out-of-band": "An out-of-band injection is one that uses a different communication channel  to launch the attack and gather the results",
    "inferential": "sql query code injected to reveal application behavior and allow the observation of possible attack vectors"
}


bashCards = {
    "cd": "changes the current working directory",
    "ls": "lists the files and branches in current directory",
    "grep": "returns directories or files matching a given description i.e. [grep Q1 home/users/quarterlyreports] "
            "returns all file names with Q1 inside it",
    "|": "called 'pipe', allows the standard output of the first command to push as standard input to following command",
    "mkdir": "makes a new directory with given name i.e. [mkdir dir] makes a directory called dir",
    "rmdir": "removes a directory with given name i.e. [rmdir dir] removes a directory called dir",
    "touch": "creates a file with given name i.e. [touch python.txt] creates a text file named touch python",
    "rm": "removes a file with given name i.e. [rm python.txt] would delete a file in current directory named "
          "python.txt",
    "mv": "moves a file with given name to given directory i.e. [mv python.txt home/analyst/programming] moves file "
          "named python.txt to programming directory",
    "cp": "copies a file with given name to given directory i.e. [cp python.txt home/analyst/programming] moves file "
          "named python.txt to programming directory, also renames file if second name is given instead of second "
          "path",
    ">": "overwrites given filename with given text i.e. [echo 'this is a string' text.txt] overwrites file text.txt "
         "with same file name and 'this is a string' as the recorded information ",
    ">>": "adds given information to given filename i.e. [echo 'this is a string' text.txt] adds 'this is a string to end of text.txt file",
    "nano": "opens a text file with the text editor nano i.e [nano text.txt] will open the text file 'text'",
    "-a": "displays hidden files in current working directory, argument for 'ls'",
    "-l": "displays file permissions in current working directory, argument for 'ls'",
    "rwx": "represents permissions for a file or directory to read/write/execute, will be a '-' if any are lacking",
    "permissions - types of owners": "user - u, group - g, other - o",
    "chmod": "change permissions of given file/dir i.e. [chmod o+r,u-x text.txt] changes permissions on text.txt file "
             "to add read perm for other and removes execute perm from user ",
    "drwxrwxrwx": "permissions readout showing target is a directory (d), user, group, and other have read/write/execute permissions",
    "sudo": "temporarily grants elevated privileges to specific users 'super user do'",
    "useradd": "adds a user to the system",
    "userdel": "removes a user from the system",
    "usermod": "modifies a users priveleges using -g and -G arguments to change group for user, or add user to "
               "additional group in tandem with -a to append or will replace current additional groups",
    "chown": "modifies ownership of a user or group. A ':' is required prior to group name",
    "groupdel": "removes a group from system, users are typically also in their own group when added",
    "man": "display information on commands and how they work i.e. [man chown] displays info on the chown command",
    "apropos": "Sort commands by specific string and return sorted information i.e. [apropos -a graph editor] will "
               "return commands that contain both graph and editor ",
    "whatis": "displays command information in a single line",
    "cmp": "compares two file and returns the first instance of difference"


}

resourceCards = {
    "https://nvd.nist.gov/": "database on common and up to date vulnerabilities",
    "https://www.sans.org/newsletters/ouch/": "reports on social engineering trends and other security topics from SANS institute",
    "https://www.scamwatch.gov.au/": "resource for news and tools on identifying, avoiding, and reporting social engineering scams",
    "https://phishingquiz.withgoogle.com/": "illustrates the difficulty of identifying phishing attacks",
    "https://www.phishing.org/": "reports on the latest phishing trends",
    "https://apwg.org/": "anti phishing work group, publishes a quarterly report on phishing trends"
}

