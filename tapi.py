def get_boards(auth_values: list):
    import requests
    from json import loads
    key = auth_values[0]
    token = auth_values[1]

    params = {
        'fields': 'id,name,shortLink',
        'key': key,
        'token': token
    }

    boards = loads(requests.get('https://api.trello.com/1/members/me/boards', params=params).text)
    return boards


def get_lists(auth_values, board_id):
    import requests
    from json import loads
    key = auth_values[0]
    token = auth_values[1]

    url = "https://api.trello.com/1/boards/" + board_id + "/lists"

    query = {
        'key': key,
        'token': token,
        'fields': 'id,name'
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )

    return loads(response.text)


def create_card(auth_values, list_id, name, description, due, complete: bool):
    import requests
    key = auth_values[0]
    token = auth_values[1]

    if complete:
        dueComplete = "true"
    else:
        dueComplete = "false"

    url = "https://api.trello.com/1/cards"

    query = {
        'key': key,
        'token': token,
        'idList': list_id,
        'name': name,
        'desc': description,
        'due': due,
        'dueComplete': dueComplete
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    if response.status_code == 200:
        return 0
    else:
        return 1

