import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class GUIGraph(FigureCanvasQTAgg):
    def __init__(self, width: int, height: int, dpi: int, nums: list):
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot()
        self.axes.plot(nums)
        super().__init__(fig)

if __name__ == '__main__':
    # draw_line(x1=3, y1=8, x2=1, y2=10)
    new_plot = GUIGraph(width=2, height=1, dpi=100, nums=[1, 1, 2, 3, 3])
    new_plot.draw()
    plt.show()