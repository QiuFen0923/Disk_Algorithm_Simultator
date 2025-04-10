# 最短服务时间优先算法
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sstf(head, list):

    numbers = list.copy()
    start = head
    head_list = [head]

    def nearest_number_index(numbers, start):
        min_diff = 2000
        nearest_index = None

        for i, num in enumerate(numbers):
            diff = abs(num - start)
            if diff < min_diff:
                min_diff = diff
                nearest_index = i

        return nearest_index

    selected_numbers = []

    while numbers:
        nearest_index = nearest_number_index(numbers, start)
        nearest_number = numbers.pop(nearest_index)
        selected_numbers.append(nearest_number)
        start = nearest_number

    num_track_move = 0

    for move in range(len(selected_numbers)):
        num_track_move += abs(head-selected_numbers[move])
        head_list.append(selected_numbers[move])
        head = selected_numbers[move]

    avg_length = num_track_move / 400

    return num_track_move, head_list, avg_length



# SSTF的动画
def sstf_ani(head_list):
    x = head_list
    y = [len(head_list) - i for i in range(len(head_list))]

    fig, ax = plt.subplots(figsize=(15, 10))

    def update(frame):
        ax.clear()
        ax.plot(x[:frame + 1], y[:frame + 1], marker='o', linestyle='-', linewidth=2, markersize=3)
        ax.set_xlabel('Head Position')
        ax.set_title('SSTF Head Movement')
        ax.grid(True)
        ax.set_yticks(range(0, 401, 50))
        ax.set_yticklabels(range(400, -1, -50))

    def init():
        ax.plot(x[0], y[0], marker='o', linestyle='-', linewidth=2)
        ax.set_xlabel('Head Position')
        ax.set_title('SSTF Head Movement')
        ax.grid(True)
        ax.set_yticks(range(0, 401, 50))
        ax.set_yticklabels(range(400, -1, -50))

    ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=False, repeat=False, interval=50)
    plt.show()