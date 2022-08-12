import random
from datetime import datetime
import os
import time

# s = dice sides
# i = dice amount
# memory = record of executed rolls in current program session


class Interface: # app interface class
    def __init__(self): # constructor
        # private variables:
        self._now = datetime.now()  # current date and time

        self._memory = [] # self.save() list of all done rolls

        self._memory.append('Roll History:') # header of the history file

        self._legend = None

        print(self.legend())

        while True:
            self._inter = input('\n~ command: ') # interface option choosing

            if self._inter == 'r':
                self.roll()
            elif self._inter == 'h':
                print(self.history())
            elif self._inter == 'l':
                print(self.legend())
            elif self._inter == 'q':
                self._quit()
                break
            else:
                print('error - invalid command')



# public metehods:
    def legend(self):
        self._legend = 'r = roll dice\nh = roll history\nl = legend\nq = save and quit'

        return self._legend



    def roll(self):
        print('dice amount: ')

        current_rolls = []

        i = int(input())

        print('dice sides: ')

        s = int(input())

        mod = int(input('modifier: '))

        print('results:')

        # loop do rollowania koscmi
        for j in range(i):
            dice = random.randint(1, s)

            print(str(dice) + ' + ' + "[" + str(mod) + "]" + ' = ', dice + mod)

            current_rolls.append(dice + mod)

        mod_string = 'mod: [' + str(mod) + ']'

        to_memory = mod_string, current_rolls

        self._memory.append(to_memory)



    def history(self):
        return self._memory



    def __save(self): # private method
        if len(self._memory) > 1:
            # generate new file name each time so history files don't overwrite
            f_name = self._now.strftime("%m-%d-%Y-%H-%M-%S")

            with open(r'roll_history_files/history_file_' + f_name + '.txt', 'w') as f_path:
                f_path.write('\n'.join(str(item) for item in self._memory))

            print('saved to history_file.txt')

        print('press enter to quit')
        input('')



    def _quit(self): # protected method
        self.__save()

        if len(self._memory) > 1: # if rolls were made the history folder will open
            print('opening folder with history files...')
            time.sleep(0.75)
            os.startfile('roll_history_files') # opening the folder where history files are located
