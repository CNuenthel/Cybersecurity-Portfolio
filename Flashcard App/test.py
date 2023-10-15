import json

def parse_text(file_name, group_name):
    with open(file_name, "r") as f:
        data = f.read()
    newlist = [item.strip() for item in data.split("â€¢") if item != "â€¢"]
    newdict = {item: "" for item in newlist[1:]}
    data = {group_name: newdict}

    with open("flashcards.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Data Parsed!")







