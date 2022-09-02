# a blocks address refers to the tower object it resides on
# a towers address refers to a label
# what kind of dummy thought this was a good naming scheme...

class Tower(object):
    def __init__(self, address):
        self.address = address
        self.population = []

    def add(self, b):
        self.population.append(b)

    def remove(self):
        self.population.pop()

    def top(self):
        return self.population[len(self.population)-1].value

    def is_full_sorted(self):
        test = []
        for block in self.population:
            test.append(block.value)
        if test == [0, 5, 4, 3, 2, 1]:
            return True
        else:
            return False

    def is_sorted(self):
        test = []
        for block in self.population:
            test.append(block.value)
        test.remove(0)

        if test == sorted(test, reverse = True):
            return True
        return False

    def pop_to_string(self):
        return [l.get_value() for l in self.population]

class Block(object):
    def __init__(self, value, t):
        self.value = value
        self.address = t
        self.previous = t
        t.add(self)

    def move_to(self, address):
        self.address.population.pop()
        address.add(self)
        self.previous = self.address
        self.address = address

    def get_value(self):
        return self.value

    def get_address(self):
        return self.address

    def get_previous(self):
        return self.previous


def full_sort(blocks, towers):
    b = 0
    # End condition of either of second towers being sorted
    print('~~~~~~~~~~~~~~~~~~')
    print("Tower A: ", tower_a.pop_to_string())
    print("Tower B: ", tower_b.pop_to_string())
    print("Tower C: ", tower_c.pop_to_string())
    print('~~~~~~~~~~~~~~~~~~')
    steps=0
    while True:
        # If the current block is free on it's tower
        blocks[b].get_value()
        if blocks[b].get_value() == blocks[b].address.top():
            for tower in towers:
                # Don't allow hopping back and forth or staying in same spot
                x = tower.address
                y = blocks[b].get_address().address
                z = blocks[b].get_previous().address
                if tower.address != blocks[b].get_previous().address and tower.address != blocks[b].get_address().address:
                    # Make sure there is a valid move
                    xx =tower.top()
                    yy = blocks[b].get_value()
                    if tower.top() == 0 or blocks[b].get_value() < tower.top():
                        blocks[b].move_to(tower)
                        steps = steps+1
                        print('~~~~~~~~~~~~~~~~~~')
                        print("Tower A: ", tower_a.pop_to_string())
                        print("Tower B: ", tower_b.pop_to_string())
                        print("Tower C: ", tower_c.pop_to_string())
                        print('~~~~~~~~~~~~~~~~~~')
                        b = -1

                        break
        if towers[1].is_full_sorted():
            print(steps)
            break
        if towers[2].is_full_sorted():
            print(steps)
            break
        b=b+1

# Towers of Hanoi
if __name__ == '__main__':
    tower_a = Tower('a')
    tower_b = Tower('b')
    tower_c = Tower('c')

    zero_a = Block(0, tower_a)
    zero_b = Block(0, tower_b)
    zero_c = Block(0, tower_c)
    five = Block(5, tower_a)
    four = Block(4, tower_a)
    three = Block(3, tower_a)
    two = Block(2, tower_a)
    one = Block(1, tower_a)

    towers = [tower_a, tower_b, tower_c]
    blocks = [five, four, three, two, one]
    full_sort(blocks,towers)
