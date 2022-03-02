from json import load
from time import perf_counter
import _game_data

letters = _game_data.get_letters()
score = _game_data.get_score()

with open('words.json', 'r') as f:
    words = load(f)
    words.sort(key=len, reverse=True)

with open('letter_points.json', 'r') as f:
    letter_points = load(f)


def calculate_score(word):
    return sum([letter_points[letter] for letter in word]) * len(word)


def check_word(word, letters):
    for letter in word:
        if letter not in letters:
            return False
        letters.remove(letter)
    return True


def solve(data):
    tries = 0
    for word in data:
        this_letters = letters[:]
        combination = []
        if not check_word(word, this_letters[:]):
            continue
        combination.append(word)
        for letter in word:
            this_letters.remove(letter)

        for word in data[1:]:
            if not check_word(word, this_letters[:]):
                continue
            combination.append(word)
            for letter in word:
                this_letters.remove(letter)

        tries += 1
        if sum([calculate_score(word) for word in combination]) == score:
            return (combination, tries)


print('Solving...')
t1 = perf_counter()
solution, tries = solve(words)
t2 = perf_counter()
print(f'The solution for the day is {solution}.')
print(f'Solved after {tries} tries in {str(t2-t1)[:5]} seconds.')
