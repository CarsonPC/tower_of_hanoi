from tkinter import *
from tkinter import ttk
import time

class Tower(object):
    def __init__(self, label):
        self.label = label
        self.population = []
        self.height = 0
        self.width = 0

    def add(self, b):
        self.population.append(b)
        self.height += self.population[-1].get_height()
    def remove(self):
        self.height -= self.population.pop().get_height()
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

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height
    def set_width(self,w):
        self.width = w

    def get_width(self):
        return self.width

    def get_label(self):
        return self.label

    def pop_to_string(self):
        return [l.get_value() for l in self.population]

class Block(object):
    def __init__(self, value, t, canvas, color, coords):
        self.canvas = canvas
        self.id = canvas.create_rectangle(coords, fill = color)
        self.x0, self.y0, self.x1, self.y1 = coords
        self.width = x1-x0
        self.height = y1-y0
        self.value = value
        self.address = t
        self.previous = t
        t.add(self)
        self.canvas.pack()
    def move_to(self, new_address, steps, text_steps, k):

        self.address.remove()
        new_address.add(self)
        self.previous = self.address
        self.address = new_address
        self.canvas.move(self.id,-self.x0,-self.y0)
        self.x0 = new_address.get_width() + (block_width-self.get_width())//2
        self.y0 = new_address.get_height()-self.get_height()
        self.canvas.move(self.id,self.x0,self.y0)
        self.canvas.itemconfig(text_steps, text="Height of Tower: {:d}".format(k)+"\nSteps: "+str(steps))


    def get_value(self):
        return self.value

    def get_address(self):
        return self.address

    def get_previous(self):
        return self.previous
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width



def full_sort(blocks, towers, block_final_layout, window, text_steps, k):

    # End condition of either of second towers being sorted
    steps = 0
    b=0

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
                        steps = steps + 1
                        blocks[b].move_to(tower, steps, text_steps, k)
                        b = -1
                        break
        b = b + 1
        time.sleep(0.01)
        window.update()
    time.sleep(2)

def create_animation_window(w, h):
    root = Tk()
    root.title("Hanoi")
    root.geometry("{:d}x{:d}".format(w, h))
    return root


def create_animation_canvas(window):
    canvas = Canvas(window)
    canvas.configure(bg="Black")
    canvas.pack(fill="both", expand=True)
    return canvas


# Towers of Hanoi
if __name__ == '__main__':
    block_limit = 9
    tower_limit = 3
    # drawing blocks
    window_width = 700
    window_height = 700
    window = create_animation_window(window_width, window_height)
    for k in range(3, block_limit):
        global block_width
        block_width = 2 * window_width // 7
        block_height = window_height // 14
        padding = block_width // 8
        x0 = padding
        x1 = padding + block_width
        y0 = window_height
        y1 = window_height - block_height
        color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "chocolate", "white"]
        coords = (x0, y0, x1, y1)
        towers = [Tower(i) for i in range(tower_limit)]

        canvas = create_animation_canvas(window)
        text_steps = canvas.create_text(5,0, font="Times 20 italic bold", anchor = "nw", text="Number of Blocks: {:d}\nSteps: {:d}".format(k, 0), fill= "Red")
        for i in range(0, tower_limit):
            Block(0, towers[i], canvas, color[i], (0,0,0,0))
        blocks = []
        for j in range(k, 0, -1):
            block = Block(j, towers[0],canvas, color[j], coords)
            blocks.append(block)
            b_width = x1 - x0
            x0 = x0 + b_width // 6
            x1 = x1 - b_width // 6
            b_height = y1 - y0
            y0 = y1
            y1 = y1 + b_height * 2 // 3
            coords = (x0, y0, x1, y1)

        towers[0].set_height(y0)
        towers[0].set_width(padding)
        towers[1].set_height(window_height)
        towers[1].set_width(2*padding+block_width)
        towers[2].set_height(window_height)
        towers[2].set_width(3*padding+2*block_width)
        block_final_layout = [b.get_value() for b in blocks]

        full_sort(blocks, towers, block_final_layout, window,text_steps, k)
        for widget in window.winfo_children():
            widget.destroy()
