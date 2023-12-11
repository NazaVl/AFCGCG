import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [list(map(int, line.split())) for line in lines]
        return np.array(points)

def find_convex_hull(points):
    hull = ConvexHull(points)
    return hull

def plot_convex_hull(points, hull, canvas_size):
    plt.figure(figsize=(canvas_size[0] / 80, canvas_size[1] / 80))
    plt.scatter(points[:, 1], points[:, 0], c='red', label='Точки')
    for simplex in hull.simplices:
        plt.plot(points[simplex, 1], points[simplex, 0], 'b-')
    plt.title('Опукла оболонка')
    plt.legend()
    plt.xlim(0, canvas_size[0])
    plt.ylim(0, canvas_size[1])
    plt.savefig('resultLab3.png')
    plt.show()

canvas_size = (960, 540)

dataset = read_dataset('DS6.txt')

hull = find_convex_hull(dataset)

plot_convex_hull(dataset, hull, canvas_size)