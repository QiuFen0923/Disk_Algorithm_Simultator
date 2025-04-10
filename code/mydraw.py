from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
from PyQt6 import QtWidgets
import matplotlib.pyplot as plt  # 这个是最重要的画图控件
import warnings



warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

# 创建 matplotlib 画图基类
class MyMplCanvas_2D(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=100):
        self.fig = plt.Figure(figsize=(width, height), dpi=dpi, facecolor='#ffffff',tight_layout=True)

        # self.fig.subplots_adjust(left=0.2, right=0.99, top=0.9, bottom=0.08)
        self.axes = self.fig.add_subplot(111)

        self.set_view_axis(False)


        FigureCanvas.__init__(self, self.fig)
        self.axes.patch.set_alpha(1)
        self.setParent(parent)
        # FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def set_view_axis(self, flag):
        self.axes.get_xaxis().set_visible(flag)
        self.axes.get_yaxis().set_visible(flag)

        self.axes.spines["top"].set_visible(flag)
        self.axes.spines["bottom"].set_visible(flag)
        self.axes.spines["left"].set_visible(flag)
        self.axes.spines["right"].set_visible(flag)



# 创建 QWidget， 把matplotlib 加入到布局
class Matplotlibwidget_2D(QtWidgets.QWidget):
    # 定义Matplotlibwidget类继承了QWidget类，绘图的主代码写在这个类里。
    def __init__(self, parent=None):
        # 不指定父子类关系，布局管理器统一管理。
        super(Matplotlibwidget_2D, self).__init__(parent)  # 继承父类

        self.initUi()

    def initUi(self):  # 对绘制的图形进行布局，并生成MyMplCanvas对象。
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.mpl_2D = MyMplCanvas_2D(self, width=1, height=1, dpi=100)

        # self.figtoolbar = NavigationToolbar(self.mpl_2D, self)


        # self.layout.addWidget(self.figtoolbar, 0, 0, 1, 1)
        self.layout.addWidget(self.mpl_2D, 0, 0, 1, 1)
        self.ani = None


    def plot_fcfs_ani(self):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        self.mpl_2D.axes.grid(True)

        plot = self.mpl_2D.axes.plot(self.x[0], self.y[0], marker='o', linestyle='-', linewidth=2)
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('FCFS Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))

        self.mpl_2D.draw()

        return plot

    def update_fcfs_plot(self, frame):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        plot = self.mpl_2D.axes.plot(self.x[:frame + 1], self.y[:frame + 1], marker='o', linestyle='-', linewidth=2, markersize=3)
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('FCFS Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))
        self.mpl_2D.draw()

        return plot

    def plot_sstf_ani(self):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        self.mpl_2D.axes.grid(True)
        plot = self.mpl_2D.axes.plot(self.x[0], self.y[0], marker='o', linestyle='-', linewidth=2, color='orange')
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('SSTF Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))

        self.mpl_2D.draw()

        return plot

    def update_sstf_plot(self, frame):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        plot = self.mpl_2D.axes.plot(self.x[:frame + 1], self.y[:frame + 1], marker='o', linestyle='-', linewidth=2, markersize=3, color='orange')
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('SSTF Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))
        self.mpl_2D.draw()

        return plot

    def plot_look_ani(self):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        self.mpl_2D.axes.grid(True)

        plot = self.mpl_2D.axes.plot(self.x[0], self.y[0], marker='o', linestyle='-', linewidth=2, color='green')
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('LOOK Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))

        self.mpl_2D.draw()

        return plot

    def update_look_plot(self, frame):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        plot = self.mpl_2D.axes.plot(self.x[:frame + 1], self.y[:frame + 1], marker='o', linestyle='-', linewidth=2, markersize=3, color='green')
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('LOOK Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))

        self.mpl_2D.draw()

        return plot

    def plot_cscan_ani(self):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        plot = self.mpl_2D.axes.plot(self.x[0], self.y[0], marker='o', linestyle='-', linewidth=2, color='red')
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('C_SCAN Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))

        self.mpl_2D.draw()

        return plot

    def update_cscan_plot(self, frame):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.set_view_axis(True)
        plot = self.mpl_2D.axes.plot(self.x[:frame + 1], self.y[:frame + 1], marker='o', linestyle='-', linewidth=2, markersize=3, color='red')
        self.mpl_2D.axes.set_xlabel('Head Position')
        self.mpl_2D.axes.set_title('C_SCAN Head Movement')
        self.mpl_2D.axes.grid(True)
        self.mpl_2D.axes.set_yticks(range(0, 401, 50))
        self.mpl_2D.axes.set_yticklabels(range(400, -1, -50))
        self.mpl_2D.draw()
        return plot

    def start_fcfs(self, head_list):
        self.head_list = head_list
        self.x = self.head_list
        self.y = [len(self.head_list) - i for i in range(len(self.head_list))]

        if self.ani is None:
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_fcfs_plot, frames=len(self.x), init_func=self.plot_fcfs_ani, blit=True, repeat=False, interval=10)
        else:
            try:
                self.ani.event_source.stop()
            except Exception:
                pass
            self.update_plot()
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_fcfs_plot, frames=len(self.x), init_func=self.plot_fcfs_ani, blit=True, repeat=False, interval=10)

    def start_sstf(self, head_list):
        self.head_list = head_list
        self.x = self.head_list
        self.y = [len(self.head_list) - i for i in range(len(self.head_list))]

        if self.ani is None:
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_sstf_plot, frames=len(self.x), init_func=self.plot_sstf_ani, blit=True, repeat=False, interval=10)
        else:
            try:
                self.ani.event_source.stop()
            except Exception:
                pass
            self.update_plot()
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_sstf_plot, frames=len(self.x), init_func=self.plot_sstf_ani, blit=True, repeat=False, interval=10)

    def start_look(self, head_list):
        self.head_list = head_list
        self.x = self.head_list
        self.y = [len(self.head_list) - i for i in range(len(self.head_list))]

        if self.ani is None:
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_look_plot, frames=len(self.x), init_func=self.plot_look_ani, blit=True, repeat=False, interval=10)
        else:
            try:
                self.ani.event_source.stop()
            except Exception:
                pass
            self.update_plot()
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_look_plot, frames=len(self.x), init_func=self.plot_look_ani, blit=True, repeat=False, interval=10)


    def start_cscan(self, head_list):
        self.head_list = head_list
        self.x = self.head_list
        self.y = [len(self.head_list) - i for i in range(len(self.head_list))]

        if self.ani is None:
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_cscan_plot, frames=len(self.x),
                                     init_func=self.plot_cscan_ani, blit=True, repeat=False, interval=10)
        else:
            try:
                self.ani.event_source.stop()
            except Exception:
                pass
            self.update_plot()
            self.ani = FuncAnimation(self.mpl_2D.fig, func=self.update_cscan_plot, frames=len(self.x),
                                     init_func=self.plot_cscan_ani, blit=True, repeat=False, interval=10)

    import matplotlib.pyplot as plt

    def plot_all_lists(self, fcfs_head_list, sstf_head_list, look_head_list, cscan_head_list):
        # Plot data for FCFS
        plt.plot(fcfs_head_list, label='FCFS')

        # Plot data for SSTF
        plt.plot(sstf_head_list, label='SSTF')

        # Plot data for LOOK
        plt.plot(look_head_list, label='LOOK')

        # Plot data for C_SCAN
        plt.plot(cscan_head_list, label='C_SCAN')

        # Set labels and title
        plt.xlabel('Index')
        plt.ylabel('Head Position')
        plt.title('Head Movement for All Algorithms')

        # Add legend
        plt.legend()

        # Show plot
        plt.show()

    # 清空画图
    def update_plot(self):
        self.mpl_2D.axes.cla()  # 清除全部绘图
        self.mpl_2D.draw()  # 将清除后的图输出到界面。




