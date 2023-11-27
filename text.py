import matplotlib.pyplot as plt

with open('DS6.txt', 'r') as f:
    lines = f.readlines()
    dataset = [tuple(map(int, line.strip().split())) for line in lines]

x_coords = [point[1] for point in dataset]
y_coords = [point[0] for point in dataset]

fig, xy = plt.subplots(figsize=(960/80, 540/80))

xy.axis('off')

xy.scatter(x_coords, y_coords)

fig.savefig('result.png')

plt.show()