import copy
import random


bashcards = {
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
    "useradd": "adds a user to the system"

}


def bashcard_rotation():
    bashcard_dict = copy.deepcopy(bashcards)

    def get_card():
        key, value = bashcard_dict.popitem()
        return key, value

    flashcards = True

    while flashcards:

        if bashcard_dict:
            card_word, card_answer = get_card()
            response = input(f"{card_word} \n")

            if response == "quit":
                flashcards = False
                print("Goodbye!")

            print(card_answer)

        else:
            print("Thats all of them!")
            flashcards = False


bashcard_rotation()