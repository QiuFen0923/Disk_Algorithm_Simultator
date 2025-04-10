# 电梯算法
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def look(head, list, num_track):
    numbers = sorted(list.copy())
    head_list = [head]

    better_num = 0
    for i in range(num_track):
        if numbers[i] >= head:
            better_num += 1

    position = num_track - better_num

    num_track_move = 0

    # 升过程
    for i in range(better_num):
        num_track_move += abs(head - numbers[position + i])
        head_list.append(numbers[position + i])
        head = numbers[position + i]

    if better_num < num_track:
        # 降过程
        for i in range(num_track - better_num):
            num_track_move += abs(head - numbers[position - i - 1])
            head_list.append(numbers[position - i - 1])
            head = numbers[position - i]

    avg_length = num_track_move / 400

    return num_track_move, head_list, avg_length


# LOOK的动画
def look_ani(head_list):
    x = head_list
    y = [len(head_list) - i for i in range(len(head_list))]

    fig, ax = plt.subplots(figsize=(15, 10))

    def update(frame):
        ax.clear()
        ax.plot(x[:frame + 1], y[:frame + 1], marker='o', linestyle='-', linewidth=2, markersize=3)
        ax.set_xlabel('Head Position')
        ax.set_title('LOOK Head Movement')
        ax.grid(True)
        ax.set_yticks(range(0, 401, 50))
        ax.set_yticklabels(range(400, -1, -50))

    def init():
        ax.plot(x[0], y[0], marker='o', linestyle='-', linewidth=2)
        ax.set_xlabel('Head Position')
        ax.set_title('LOOK Head Movement')
        ax.grid(True)
        ax.set_yticks(range(0, 401, 50))
        ax.set_yticklabels(range(400, -1, -50))

    ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=False, repeat=False, interval=50)
    plt.show()
