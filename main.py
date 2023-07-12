import role
import random
from decorator import looger

def get_user_choice():
    user_choice = input("Enter betwenn (r , s, p) : ")
    if user_choice not in role.ROLE:
        print("invalid value please inter the valid value")
        return get_user_choice()
    return user_choice


def get_system_choice():
    choice = random.choice(role.ROLE)
    return choice


def winner(human, comp):
    temp = {human, comp}
    if len(temp) == 1:
        return None
    else:
        return role.WINNER[tuple(sorted(temp))]


def update_dast(user, system):
    if user == 3:
        role.dast['user'] += 1
    elif system ==3:
        role.dast['system'] += 1


def play_game():
    counter_time = {'user': 0, 'system': 0}
    while counter_time['user'] < 3 and counter_time['system'] < 3:
        user = get_user_choice()
        system = get_system_choice()
        win = winner(user, system)
        if win == user:
            msg = "You Win"
            counter_time['user'] += 1
        elif win == system:
            msg = "You Lose"
            counter_time['system'] += 1
        elif win == None:
            msg = "Drow"
        print(f"the user : {user}\nsystem : {system}\nwinner : {msg}")
    update_dast(counter_time['user'], counter_time['system'])
    print(30 * '#')
    print(f"the user {role.dast['user']}")
    print(f"the system {role.dast['system']}")
    print(30 * '#')
    agein = input("Do You Want To play Again (Y,N) : ")
    if agein == 'y':
        play_game()

@looger
def play():
    play_game()

if __name__ == "__main__":
    play()
