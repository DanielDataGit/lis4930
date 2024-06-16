# modify rectangle

import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Rectangle:
    """ A class to manufacture rectangle objects """

def __init__(self, posn, w, h):
    """ Initialize rectangle at posn, with width w, height h """
    self.corner = posn
    self.width = w
    self.height = h

def __str__(self):
    return "({0}, {1}, {2})"
    format(self.corner, self.width, self.height)

fig, ax = plt.subplots()
box = patches.Rectangle((0, 0), 100, 200, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(box)
plt.xlim(-10, 120)
plt.ylim(-10, 220)
plt.show()

bomb = patches.Rectangle((100, 80), 5, 10, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(box)
plt.xlim(90, 110)
plt.ylim(70, 90)
plt.show()

def create_rectangle( corner, width, height):
    return Rectangle( corner, width, height)

r1 = create_rectangle(10, 20, 30, 40)

print(str_rectangle(r1))


