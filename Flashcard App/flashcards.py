
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
    "https://apwg.org/": "anti phishing work group, publishes a quarterly report on phishing trends",
    "https://www.virustotal.com/gui/home/upload": "service that allows anyone to analyze suspicous files, domains, URLs, and IPs for malicious content"
}

threatModel = {
    "step1": "define the scope",
    "step2": "identify threats",
    "step3": "characterize environments",
    "step4": "analyze threats",
    "step5": "mitigate risks",
    "step6": "evaluate findings",
    "pasta model": "process for attack simulation and threat analysis"
}

alertAndEventManagement = {
    "intrusion detection system (IDS)": "detects malicious activity, logs activity, generates alerts, observes but does not interfere with attackers (zeek, suricata, snort, sagan)",
    "intrusion prevention system (IPS)": "detects malicious activity, prevents intrusions, logs activity, generates alerts, can halt a system from operating to prevent intrusion",
    "endpoint detection and response (EDR)": "monitor, record, and analyze endpoint system activity to identify, alert, and respond to suspicious activity",
    "true positive": "an alert that correctly identifies an attack",
    "true negative": "state where there is no detection of malicious activity, no alert is triggered",
    "false positive": "an alert that incorrectly detects the presence of a threat",
    "false negative": "state where the presence of malicious activity is not detected",
    "siem": "security information and event management, a tool used to aggregate, normalize and analyze data",
    "siem tool products": "AlienVault, Chronicle, Elastic, Exabeam, IBM QRadar, LogRhythm, Splunk",
    "security orchestration, automation, and response": "a collection of tools, applications, and workflows used to automate and respond to security events",
    "indicators of compromise (IOC)": "observable evidence that suggests signs of a potential security incident, such as an admin account being created after work hours or a usb stick in an unsupervised work station",
    "network protocol analyzers": "sometimes called packet sniffers, tools designed to capture and analyze data traffic within a network",
    "data packet": "basic unit of information that travels from one device to another within a network",
    "network interface card (NIC)": "hardware that connects a computer to a network",
    "packet capture formats": "Libpcap (Linux, MacOS), WinPcap (older format for windows), Npcap (Windows), PCAPng (capture packets and store data simultaneously)"
}

NIST = {
    "identify": "identify assets to protect",
    "protect": "implement tools to protect the attack surface of assets",
    "detect": "detect malicious threats",
    "respond": "remediate open attack vectors, and record damage",
    "recover": "return systems to normal working order and establish policies to prevent future intrusion"
}

ipv4PacketFields = {
    "version": "which version of ip is being used ipv4 in this instance",
    "internet header length (IHL)": "length of header and options",
    "type of service (TOS)": "provides information on packet priority for delivery",
    "total length": "identifies the length of the entire packet including headers and data",
    "identification, flags, fragment offset": "deal with information related to fragmentation, ip packet is broken into chunks, transferred and reassembeld",
    "time to live (TTL)": "determines how long a packet can live before it gets dropped",
    "protocol" : "specifies what protocol is being used, i.e. tcp = 6",
    "header checksum": "stores a checksum value which is used to determine if there are any errors in the header",
    "source ip address": "sender address of data packet",
    "destination ip address": "receiver address of data packet",
    "options": "not required, used for network troubleshooting"
}

ipv6PacketFields = {
    "version": "which version of ip is being used, ipv6 in this instance",
    "traffic class": "similar to type of service, provides information on packet priority for delivery",
    "flow label": "identifies the packets of a flow; a sequence of packets sent from a specific address",
    "payload length": "specifies length of data portion of the packet",
    "next header": "the type of header that follows the ipv6 header, such as TCP",
    "hop limit": "limits how long a packet can travel before being dropped",
    "source address": "sender address of data packet",
    "destination address": "receiver address of data packet"
}

wireshark = {
    "filter for ip address": "ip.addr == {address}, ip.src == {address} (select ip source), ip.dst == {address} (select ip destination)",
    "filter for mac address": "eth.addr == {address}",
    "filter for ports": "udp.port == 53, tcp.port ==25",

}

logs = {
    "syslogs": "log format that contains a header, structure data, and method",
    "javascript object notation": "json, uses key value pairs to structure data",
    "comma seperated values": "csv files, similar to cell structure of spreadsheets",
    "extensible markup language": "xml, stores data in tagged format utilizing parent and child tags",
    "common event format": "uses key-value pairs to structure data and identify fields and their corresponding values"
}
