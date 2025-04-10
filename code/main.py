from FCFS import *
from SSTF import *
from LOOK import *
from C_SCAN import *

import random



class test:

    # 生成随机磁道号
    def generate_track_numbers(position_head):
        # 记录已生成的磁道号，避免重复
        position = set()
        # 50%位于 0～499
        while len(position) < 200:
            num = random.randint(0, 499)
            if num != position_head:
                position.add(num)
            if len(position) == 200:
                break
            if num + 1 <= 499 and num + 1 != position_head:
                position.add(num + 1)  # 将随机数+1后也添加到序列中

        # 25%分布在 500～999
        while len(position) < 300:
            num = random.randint(500, 999)
            if num != position_head:
                position.add(num)
            if len(position) == 300:
                break
            if num + 1 <= 999 and num + 1 != position_head:
                position.add(num + 1)

        # 25%分布在 1000～1499
        while len(position) < 400:
            num = random.randint(1000, 1499)
            if num != position_head:
                position.add(num)
            if len(position) == 400:
                break
            if num + 1 <= 1499 and num + 1 != position_head:
                position.add(num + 1)

        position = list(position)
        position = [int(i) for i in position]

        # 打乱列表顺序
        random.shuffle(position)
        return position


    # 计算磁头移动数
    def calculate(position_head, position_point):
        # 先入先出算法
        num_fcfs, head_fcfs, avg_fcfs = fcfs(position_head, position_point)
        print(num_fcfs)
        # fcfs_animation(head_fcfs)
        print(avg_fcfs)

        # 最短服务时间优先算法
        num_sstf, head_sstf, avg_sstf = sstf(position_head, position_point)
        print(num_sstf)
        # sstf_animation(head_sstf)
        print(avg_sstf)

        # 电梯算法
        num_look, head_look, avg_look = look(position_head, position_point, num_track=400)
        print(num_look)
        # print(head_look)
        # look_animation(head_look)
        print(avg_look)

        # 循环扫描算法
        num_c_scan, head_c_scan, avg_c_scan = c_scan(position_head, position_point, num_track=400)
        print(num_c_scan)
        # c_scan_animation(head_c_scan)
        print(avg_c_scan)
