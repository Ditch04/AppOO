from Player import Player
from Fine import Fine
from Pot import Pot
from Team import Team

if __name__ == '__main__':
    team = Team()
    comm = input('Pour ajouter un joueur tapez j, pour ajouter une amende tapez a\n')
    if comm == 'j':
        firstname = input('Prénom du joueur :\n')
        player1 = Player(firstname)
        team.add_player_to_team(player1)

    elif comm == 'a':
        player_fined = input("Prénom du joueur à qui l'amende est adressée\n")
        fine = input("Quel est l'intitulé de l'amende ?\n")

    else:
        print('commande invalide, recommencez\n')

    print(team.team_list)

