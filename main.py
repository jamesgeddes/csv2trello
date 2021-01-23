input_filename = "import"


def welcome():
    print("Hello and thanks for using CSV2Trello")
    print("This super simple program does what it says on the ti...tle")
    print("It takes your CSV and makes cards in Trello")


def ask_user():
    proceed = "n"
    while proceed != "y":
        user_input = input("Please enter value: ")
        print("I got this:")
        print(user_input)
        print("Is that correct?")
        proceed = input("y or n: ")
    return user_input


def user_confirm():
    response = "n"
    while response != "y":
        print("Please confirm")
        response = input("y or n: ")
    return True


def get_keys():
    print("First lets get your Trello keys")
    print("Please go here")
    print("https://trello.com/app-key")
    print("What is your Developer API Key?")
    trello_dev_key = ask_user()

    print("What is your Developer API token?")
    trello_dev_token = ask_user()
    return trello_dev_key, trello_dev_token


def write_env(key, token):
    from filehandle import write_file
    content = ["TRELLO_DEV_KEY=" + key, "TRELLO_DEV_TOKEN=" + token]
    write_file(".env", content)
    print("Saved keys to .env")


def keys():
    from dotenv import load_dotenv
    import os

    load_dotenv()
    trello_dev_key = os.getenv("TRELLO_DEV_KEY")
    trello_dev_token = os.getenv("TRELLO_DEV_TOKEN")

    if trello_dev_key and trello_dev_token:
        print("Found your key:   " + trello_dev_key)
        print("Found your token: " + trello_dev_token)
        key_values = trello_dev_key, trello_dev_token
        return key_values
    else:
        key_values = get_keys()
        write_env(key_values[0], key_values[1])
        return key_values


def main():
    from tapi import get_boards, get_lists, create_card
    from filehandle import get_csv

    welcome()
    trello_keys = keys()
    print("\nIs your " + input_filename + ".csv file ready and in the same directory as CSV2Trello?")
    user_confirm()
    print("Here are all the boards that you are a member of.")

    boards = get_boards(trello_keys)
    for board in enumerate(boards):
        print(str(board[0] + 1) + " " + "http://trello.com/b/" + board[1]["shortLink"] + " " + board[1]["name"])

    print("Which board number do you want to add import to?")
    board_number = int(ask_user()) - 1
    board_selected = boards[board_number]
    print("\nYou selected board '" + board_selected["name"] + "'")

    print("Here are all the lists from '" + board_selected["name"] + "'")
    lists = get_lists(trello_keys, board_selected["id"])
    for item in enumerate(lists):
        print(str(item[0] + 1) + " " + item[1]["name"])
    print("Which list number are we importing to today?")
    list_number = int(ask_user()) - 1
    list_selected = lists[list_number]
    print("\nYou selected the '" + list_selected["name"] + "' list from your '" + board_selected["name"] + "' board")

    try:
        cards = get_csv("import")
    except FileNotFoundError:
        print("Could not find your " + input_filename + ".csv file. Please hang up and try again.")
        raise SystemExit()
    cards.pop(0)
    input("Last step! Putting your " + input_filename + ".csv file on Trello. Press enter to continue...")
    for card in cards:
        name = card[0]
        description = card[1]
        due = card[2]
        if card[3] == "TRUE":
            completed = True
        else:
            completed = False

        trello_create = create_card(trello_keys,
                                    list_selected["id"],
                                    name,
                                    description,
                                    due,
                                    completed)
        if trello_create == 0:
            print("Success: " + name)
        else:
            print("ERROR: " + name)

    print("All done!")
    print("If that saved you some time, please consider buying me a coffee.")
    print("Amazon and PayPal links at http://JamesGeddes.pro")
    print("Thanks!")



main()
