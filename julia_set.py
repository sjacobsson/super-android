import numpy as np
import itertools
import random
import threading
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Image width and height in pixels; parameters for the plot
width, height = 1000, 1000
i_max = 1000
zabs_max = 10.0
xmin, xmax = -1.5, 1.5
xwidth = xmax - xmin
ymin, ymax = -1.5, 1.5
yheight = ymax - ymin

# Map pixel position to a point in the complex plane
def z(i, j):
    return complex(
        i / width * xwidth + xmin,
        j / height * yheight + ymin
    )

def julia(z, c=complex(-0.1, 0.65)):
    i = 0

    while abs(z) <= zabs_max and i < i_max:
        z = z**2 + c
        i += 1

    # Do the iterations
    ratio = i / i_max

    return ratio

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

J = np.zeros((width, height))

class FractalThread (threading.Thread):
    def __init__(self, number, width, height, coords):
        self.number, self.width, self.height, self.coords = number, width, height, coords
        threading.Thread.__init__(self)

    def run(self):
        print(f"Starting {self.number}")
        number, width, height, coords = self.number, self.width, self.height, self.coords

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(f"192.168.0.{number}", port=2222, pkey=paramiko.Ed25519Key.from_private_key_file("/home/arne/.ssh/id_phones"))
        _, out, _ = ssh.exec_command(f"su -c 'super\ android/a.out {int(width / 2)} {height} {' '.join(map(str, coords))}'")
        if number == 1: # TODO: The regions should be generalised
            J[int(width / 2):, :] = np.reshape([float(s) for s in out.read().splitlines()], (int(width / 2), height))
        else:
            J[:int(width / 2), :] = np.reshape([float(s) for s in out.read().splitlines()], (int(width / 2), height))
        print(f"Ending {number}")

threads = [
    FractalThread(1, width, height, [0, 1.5, -1.5, -1.5]),
    FractalThread(2, width, height, [1.5, 1.5, 0, -1.5]),
]

use_phones = True
if use_phones:
    for t in threads: t.start()
    for t in threads: t.join()
else:
    indices = list(itertools.product(range(width), range(height)))
    batches = np.array_split(indices, 10)
    for b in batches:
        for (i, j) in b:
            J[i, j] = julia(z(i, j))

fig, ax = plt.subplots()
ax.imshow(J, interpolation='nearest', cmap=cm.hot)
plt.show()

