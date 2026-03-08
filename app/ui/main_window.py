from PySide6 import QtCore, QtWidgets, QtGui
from ui.widgets.tool_panel import ToolPanel
from ui.widgets.grid_canvas import GridCanvas
from ui.widgets.plot_panel import PlotPanel



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RL Algorithms Demo")
        self.resize(1200, 900)

        self._build_ui()

    def _build_ui(self) -> None:
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        root_layout = QtWidgets.QHBoxLayout(central)
        root_layout.setContentsMargins(12, 12, 12, 12)
        root_layout.setSpacing(12)

        left_panel = ToolPanel()
        right_panel = self._build_right_panel()

        left_panel.setFixedWidth(300)
        root_layout.addWidget(left_panel)
        root_layout.addWidget(right_panel, stretch=1)

 
    def _build_right_panel(self) -> QtWidgets.QWidget:
        panel = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(panel)
        layout.setSpacing(12)

        canvas = GridCanvas()
        plot = PlotPanel()

        layout.addWidget(canvas, stretch=3)
        layout.addWidget(plot, stretch=2)

        return panel
        


