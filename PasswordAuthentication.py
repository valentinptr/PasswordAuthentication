import getpass
from dataset import database_addUser_avant


def add_user(database, login, mdp):
    if type(database) != dict:
        print(f"add_user : Erreur de type pour le paramètre : database")
        return -1
    if type(login) != str:
        print(f"add_user : Erreur de type pour le paramètre : login")
        return -2
    if type(mdp) != str:
        print(f"add_user : Erreur de type pour le paramètre : mdp")
        return -3

    if login in database:
        print("add_user : Login déjà présent dans la base de donnée !")
        return -4
    else:
        database[login] = mdp
        return database


def delete_user(database, login):
    if type(database) != dict:
        print(f"delete_user : Erreur de type pour le paramètre : database")
        return -1
    if type(login) != str:
        print(f"delete_user : Erreur de type pour le paramètre : login")
        return -2

    if login not in database:
        print("delete_user : User inconnu !")
        return -3
    else:
        del database[login]
        return database


def update_password(database, login, mdp):
    if type(database) != dict:
        print(f"update_password : Erreur de type pour le paramètre : database")
        return -1
    if type(login) != str:
        print(f"update_password : Erreur de type pour le paramètre : login")
        return -2
    if type(mdp) != str:
        print(f"update_password : Erreur de type pour le paramètre : mdp")
        return -3

    if login not in database:
        print("update_password : User inconnu !")
        return -4
    else:
        if database[login] == mdp:
            print("update_password : Mdp identique")
            return -5
        else:
            database[login] = mdp
            return database


def authent(database):
    login = input('Entrez votre login : ')

    while login not in database:
        login = input('Entrez votre login valide : ')

    mdp = getpass.getpass(prompt=f'Entrez le mot de passe du login : {login} ', stream=None)

    while mdp != database[login]:
        mdp = getpass.getpass(prompt=f'Entrez le mot de passe du login : {login} de nouveau ', stream=None)

    print('Bienvenu !')


authent(database_addUser_avant)
