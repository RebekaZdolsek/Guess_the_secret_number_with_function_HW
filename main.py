from random import randint

MAX_NUMBER_OF_ATTEMPTS = 3
MIN_NUMBER = 1
MAX_NUMBER = 5

class Player:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.best_score = 0

    def get_full_name(self):
        print(f'{self.name} {self.surname} from class')

class HighScore:
    def __init__(self):
        self.scores = {}

    def add_score(self, player_name, score):
        if player_name not in self.scores or score > self.scores[player_name]:
            self.scores[player_name] = score

    def get_best_score(self, player_name):
        return self.scores.get(player_name, 0)


def play_game(player, high_scores):
    print(f'Hello player {player.name} {player.surname}. '
          f'Let the games begin. Your best score is: {high_scores.get_best_score(player.name)}')
    secret_number = randint(MIN_NUMBER, MAX_NUMBER)

    remaining_attempts = MAX_NUMBER_OF_ATTEMPTS

    for attempt in range(MAX_NUMBER_OF_ATTEMPTS):
        guess = int(input("Guess the secret number: "))

        remaining_attempts = remaining_attempts - 1

        if guess == secret_number:
            print("Congrats!")
            high_scores.add_score(player.name, remaining_attempts)
            player.best_score = high_scores.get_best_score(player.name)
            break

        print("Oh no, that was not it.")

        if remaining_attempts == 0:
            print(f"To bad, you used all attempts. The secret number was {secret_number}")

player = Player(input("What is your name? "), input("What is your surname? "))
high_scores = HighScore()

while True:
    play_game(player, high_scores)

    continue_playing = input("Would you like to play another (yes/no)? ")

    if continue_playing.lower() == "no":
        break

print(f"Nice playing with you. Your best score was: {player.best_score}")