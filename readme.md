# CSV2Trello

I use Trello for ruddy everything, from big stuff like organising projects, to little stuff like taking the bins out. I clearly do like Trello a lot, but I wanted to be able to generate a list of tasks in a spreadsheet and then import that into Trello. I think it's a bit odd that this does not natively exist in Trello, so I've made a tool that can do it for you.

This is a super simple tool that takes your `name, description, due, completed` CSV and throws it at Trello. That's all it does, nothing fancy.

If you find a bug, please submit a ticket.

## Some Nerdiness Required
It's currently designed as CLI for Python3, so you will need to install Python3 before you can run this. You will also need to generate a Trello [Developer API key & token](https://trello.com/app-key). I appreciate that this is not particularly user-friendly, so I'll slowly make it better. I also only speak English, so apologies that it's not available in other languages.

## Running it
1. Install [Python3](https://www.python.org/downloads/)
1. run `git clone https://github.com/jamesgeddes/csv2trello.git` or download & extract the [zip](https://github.com/jamesgeddes/csv2trello/archive/main.zip)
1. Install the project dependencies `pip install -r requirements.txt`
1. From your favourite spreadsheet software, export a CSV with the headings `name`, `description`, `due`, and `completed`
1. Place the CSV in the same directory/folder as `main.py`
1. run `python3 main.py`
1. Do what it tells you to do.
1. Check your Trello board!

## CSV Content
`name`
The title of the card. Any text is good. Not sure what the character limit is but don't go nuts. Required. If empty, entire card/row will be ignored.

`description`
The description of the card. Again, any text is good and probably has a big character limit, but probably best avoiding "War and Peace". Ignored if empty.

`due`
DateTime that this card is due by. **Must** be in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Because why would any [sensible person](https://xkcd.com/1179/) not use that date format? Ignored if empty. "YYYY-MM-DDTHH:mm:ssZ"

`completed`
Is this card complete? If this card is already done, this should be `TRUE`, if not, it's `FALSE`. If empty, we assume it's `FALSE`.

## Contributions

It would seem that most of the [existing tools](https://help.trello.com/article/751-importing-data-into-trello) that can do this are not free. As this tool is entirely free and open source, if you find it helpful, if it saved you some time perhaps, I would be tremendously grateful for any contributions - you might like to take a look at my [Amazon gift list](https://www.amazon.co.uk/hz/wishlist/ls/WS5TGJQ9K8BS?ref_=wl_share) for example.