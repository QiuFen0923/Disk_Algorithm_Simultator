# 先入先出算法
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QGraphicsView
from matplotlib.animation import FuncAnimation


def fcfs(head, list):
    head_list = [head]
    num_track_move = 0

    for move in range(len(list)):
        num_track_move += abs(head-list[move])
        head_list.append(list[move])
        head = list[move]

    avg_length = num_track_move / 400

    return num_track_move, head_list, avg_length


# FCFS的动画
def fcfs_ani(head_list):
    x = head_list
    y = [len(head_list) - i for i in range(len(head_list))]

    def update(frame):
        ax.clear()
        ax.plot(x[:frame+1], y[:frame+1], marker='o', linestyle='-', linewidth=2, markersize=3)
        ax.set_xlabel('Head Position')
        ax.set_title('FCFS Head Movement')
        ax.grid(True)
        ax.set_yticks(range(0, 401, 50))
        ax.set_yticklabels(range(400, -1, -50))

    def init():
        ax.plot(x[0], y[0], marker='o', linestyle='-', linewidth=2)
        ax.set_xlabel('Head Position')
        ax.set_title('FCFS Head Movement')
        ax.grid(True)
        ax.set_yticks(range(0, 401, 50))
        ax.set_yticklabels(range(400, -1, -50))

    fig, ax = plt.subplots(figsize=(8, 10))
    ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=False, repeat=False, interval=50)
    plt.show()




