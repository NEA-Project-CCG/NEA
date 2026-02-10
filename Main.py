from Gameloop import Gameloop
from Login import safety_login


def main():
    login = safety_login()
    login.begin()
    Gameloop.gameloop(login.Player_id)


if __name__ == '__main__':
    main()

