import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000

from matplotlib import animation, rc
#from IPython.display import HTML
from matplotlib import collections  as mc

test_5 = '.#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n.#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n#.#.#.#####.####.###\n###.##.####.##.#..##'

test = test_5.split('\n')
cleaned = []
for row in test:
    cleaned_row = []
    for item in row:
        item = 1 if item == '#' else 0
        cleaned_row.append(item)
    cleaned.append(cleaned_row)

map = np.array(cleaned)
h,w = map.shape
yy, xx = np.where(map == 1)

def cool_plot(j, xx, yy, map):
    x1, y1 = j
    asteroid_lines_xx = []
    asteroid_lines_yy = []
    asteroids_xx = []
    asteroids_yy = []
    this_asteroids_vis_count = 0

    for (x2, y2) in zip(xx, yy):
        if (x1, y1) != (x2, y2):
            # y = m*x + b
            # Determine the equation of the line between the two asteroids
            delta_y = y2 - y1
            delta_x = x2 - x1
            # Check to see if any other asteroids are on that line, if so (x2,y2) is blocked.
            count = 0
            for (xcheck, ycheck) in zip(xx, yy):
                s1 = ''
                s2 = ''
                if ((xcheck, ycheck) != (x1, y1)) and ((xcheck, ycheck) != (x2, y2)):
                    if (min(x1, x2) <= xcheck <= max(x1, x2)) and (min(y1, y2) <= ycheck <= max(y1, y2)):
                        if (delta_x == 0):
                            if x1 == xcheck:
                                s1 = f'equation for line {x1, y1}---{x2, y2}: x={x1}'
                                s2 = f'asteroid at {xcheck, ycheck} on this line'
                                count += 1
                        elif (delta_y == 0):
                            if y1 == ycheck:
                                s1 = f'equation for line {x1, y1}---{x2, y2}: x={y1}'
                                s2 = f'asteroid at {xcheck, ycheck} on this line'
                                count += 1
                        else:
                            m = (y2 - y1) / (x2 - x1)
                            b = y1 - m * x1
                            if (ycheck == m * xcheck + b):
                                s1 = f'equation for line {x1, y1}---{x2, y2}: y = {m}*x + {b}'
                                s2 = f'asteroid at {xcheck, ycheck} on this line'
                                count += 1
                        # if s1:
                        # print(s1)
                        # print(s2)
            if count == 0:
                # print(f'Asteroid {x1, y1} has a clear path to: {x2,y2}')
                this_asteroids_vis_count += 1
                asteroid_lines_xx.append((x1, x2))
                asteroid_lines_yy.append((y1, y2))
                asteroids_xx.append(x2)
                asteroids_yy.append(y2)

    return asteroids_xx, asteroids_yy, asteroid_lines_xx, asteroid_lines_yy

##### initialization function: plot the background of each frame
def init():
    return (line1, line2, line3,)

# animation function. This is called sequentially
def animate(j, xx, yy, map):
    asteroids_xx, asteroids_yy, asteroid_lines_xx, asteroid_lines_yy = cool_plot(j, xx, yy, map)
    line2.set_data(asteroid_lines_xx, asteroid_lines_yy)
    line3.set_data(asteroids_xx, asteroids_yy)
    print('here')
    return (line1, line2, line3,)

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.invert_yaxis()
ax.set_xlim(-1,w+1)
ax.set_ylim(h+1,-1)
ax.axis('off')
line1, = ax.plot(xx, yy, color='blue', linestyle='', marker='o', markersize=1)
line2, = ax.plot([], [], color='red', linestyle='dotted', linewidth=0.8)
line3, = ax.plot([], [], color='green', linestyle='', marker='o', markersize=4)

frames = [(x,y) for (x,y) in zip(xx,yy)]

# call the animator. blit=True means only re-draw the parts that have changed.
params = {
    'fig': fig,
    'func': animate,
    'frames': frames,
    'init_func': init,
    'interval': 200,
    'blit': True,
    'fargs': (xx, yy, map,),
    'cache_frame_data': False,
}
anim = animation.FuncAnimation(**params)
plt.close('all')
anim.save('test.gif', writer='imagemagick', fps=10)
#HTML(anim.to_html5_video())
# anim.save('basic_animation.mp4', fps=30)