class Rolls:
    '''Class to separate the individual rolls
    '''
    def __init__(self, rolls):
        self.len = len(rolls)
        self.rolls = [
            {'red': 0, 'green': 0, 'blue': 0} for _ in range(self.len)]

        self.populate(rolls)

    def populate(self, rolls):
        '''
        Goes through every roll and populates list of each roll and each color.
        '''
        rolls = rolls.strip().split(';')

        for i, roll in enumerate(rolls):
            roll = roll.split(',')
            for color in roll:
                num, rgb = color.split()
                self.rolls[i][rgb] = int(num)

    def __getitem__(self, key):
        return self.rolls[key]

    def __len__(self):
        return self.len


sum_of_ids = 0
RED = 12
GREEN = 13
BLUE = 14

with open('input.txt') as f:
    for line in f:
        game, rolls = line.split(':')
        curr_id = int(game.split()[1])

        rolls = Rolls(rolls)
        valid = True

        for i in range(len(rolls)):
            if rolls[i]['red'] > RED:
                valid = False
                break
            elif rolls[i]['green'] > GREEN:
                valid = False
                break
            elif rolls[i]['blue'] > BLUE:
                valid = False
                break
        if valid:
            sum_of_ids += curr_id

print(sum_of_ids)
