from trello import TrelloClient

client = TrelloClient(
    api_key='your-key',
    api_secret='your-secret',
    token='your-oauth-token-key',
    token_secret='your-oauth-token-secret'
)

all_boards = client.list_boards()
last_board = all_boards[-1]
print(last_board.name)