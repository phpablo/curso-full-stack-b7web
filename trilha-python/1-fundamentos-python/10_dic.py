my_games_list = [
    {
        "nome": "The Last of Us", "data_lancamento": "2013"
    }
]
def game_list(name, release_date):
    my_games_list.append({"nome": name, "data_lancamento": release_date})

game_list("The Witcher 3", "2015")
game_list("GTA V", "2013")

print(my_games_list)
