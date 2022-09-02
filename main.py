# a blocks address refers to the tower object it resides on
# a towers address refers to a label
# what kind of dummy thought this was a good naming scheme...

class Tower(object):
    def __init__(self, label):
        self.label = label
        self.population = []

    def add(self, b):
        self.population.append(b)

    def remove(self):
        self.population.pop()

    def top(self):
        return self.population[len(self.population) - 1].value

    def is_full_sorted(self, bfl):
        test = []
        for block in self.population:
            test.append(block.value)
        if test[1:] == bfl:
            return True
        else:
            return False

    def get_label(self):
        return self.label

    def pop_to_string(self):
        return [l.get_value() for l in self.population]


class Block(object):
    def __init__(self, value, t):
        self.value = value
        self.address = t
        self.previous = t
        t.add(self)

    def move_to(self, new_address):
        self.address.population.pop()
        new_address.add(self)
        self.previous = self.address
        self.address = new_address

    def get_value(self):
        return self.value

    def get_address(self):
        return self.address

    def get_previous(self):
        return self.previous


def full_sort(blocks, towers, block_final_layout):
    b = 0
    # End condition of either of second towers being sorted
    steps = 0
    while not towers[1].is_full_sorted(block_final_layout) and not towers[2].is_full_sorted(
            block_final_layout):
        # If the current block is free on it's tower
        if blocks[b].get_value() == blocks[b].address.top():
            for tower in towers:
                # Don't allow hopping back and forth or staying in same spot
                if tower.get_label() != blocks[b].get_previous().get_label() and tower.get_label() != blocks[
                    b].get_address().get_label():
                    # Make sure there is a valid move
                    if tower.top() == 0 or blocks[b].get_value() < tower.top():
                        blocks[b].move_to(tower)
                        steps = steps + 1

                        for t in towers:
                            print(t.pop_to_string())
                        print("~~~~~~~~~~~~~~~~~~")

                        b = -1

                        break
        b = b + 1
    print("Iterations: {:d}".format(steps))


# Towers of Hanoi
if __name__ == '__main__':
    block_limit = 5
    tower_limit = 3

    towers = [Tower(i) for i in range(tower_limit)]

    for i in range(0, tower_limit):
        Block(0, towers[i])
    blocks = [Block(i, towers[0]) for i in range(block_limit, 0, -1)]
    block_final_layout = [b.get_value() for b in blocks]
    full_sort(blocks, towers, block_final_layout)
