class Elf:
    def __init__(self, current_index):
        self.current_index = current_index

    def cycle(self, scoreboard):
        new_index = self.current_index + scoreboard[self.current_index] + 1

        if new_index >= scoreboard.__len__():
            self.current_index = new_index % scoreboard.__len__()
        else:
            self.current_index = new_index

