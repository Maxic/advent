class Cart:
    def __init__(self, x_pos, y_pos, direction):
        self.x = x_pos
        self.y = y_pos
        self.direction = direction
        self.turn = 'l'
        self.state = 'active'

    def execute_turn(self):
        if self.turn == 'l':
            self.turn = 's'
            return 'l'
        elif self.turn == 's':
            self.turn = 'r'
            return 's'
        else:
            self.turn = 'l'
            return 'r'

    def step(self, cart_map):
        if self.direction == '^':

            self.y -= 1
            next_tile = cart_map[self.y][self.x]

            if next_tile == '/':
                self.direction = '>'
            elif next_tile == '\\':
                self.direction = '<'
            elif next_tile == '+':
                turn = self.execute_turn()
                if turn == 'l':
                    self.direction = '<'
                elif turn == 'r':
                    self.direction = '>'

            if next_tile in ['^', '>', '<', 'v']:
                self.state = 'crashed'
                self.direction = 'X'

            return (self.x, self.y), self.direction, self.state

        elif self.direction == '>':

            self.x += 1
            next_tile = cart_map[self.y][self.x]

            if next_tile == '/':
                self.direction = '^'
            elif next_tile == '\\':
                self.direction = 'v'
            elif next_tile == '+':
                turn = self.execute_turn()
                if turn == 'l':
                    self.direction = '^'
                elif turn == 'r':
                    self.direction = 'v'

            if next_tile in ['^', '>', '<', 'v']:
                self.state = 'crashed'
                self.direction = 'X'

            return (self.x, self.y), self.direction, self.state

        elif self.direction == '<':

            self.x -= 1
            next_tile = cart_map[self.y][self.x]

            if next_tile == '/':
                self.direction = 'v'
            elif next_tile == '\\':
                self.direction = '^'
            elif next_tile == '+':
                turn = self.execute_turn()
                if turn == 'l':
                    self.direction = 'v'
                elif turn == 'r':
                    self.direction = '^'

            if next_tile in ['^', '>', '<', 'v']:
                self.state = 'crashed'
                self.direction = 'X'

            return (self.x, self.y), self.direction, self.state
        else:

            self.y += 1
            next_tile = cart_map[self.y][self.x]

            if next_tile == '/':
                self.direction = '<'
            elif next_tile == '\\':
                self.direction = '>'
            elif next_tile == '+':
                turn = self.execute_turn()
                if turn == 'l':
                    self.direction = '>'
                elif turn == 'r':
                    self.direction = '<'

            if next_tile in ['^', '>', '<', 'v']:
                self.state = 'crashed'
                self.direction = 'X'

            return (self.x, self.y), self.direction, self.state









