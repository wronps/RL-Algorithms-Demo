from PySide6 import QtCore, QtWidgets, QtGui
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

        left_panel = self._build_left_panel()
        right_panel = self._build_right_panel()

        left_panel.setFixedWidth(300)
        root_layout.addWidget(left_panel)
        root_layout.addWidget(right_panel, stretch=1)

    def _build_left_panel(self) -> QtWidgets.QWidget:
        panel = QtWidgets.QFrame()
        panel.setFrameShape(QtWidgets.QFrame.StyledPanel)

        layout = QtWidgets.QVBoxLayout(panel)
        layout.setSpacing(12)

        title = QtWidgets.QLabel("Tool Panel")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        desc = QtWidgets.QLabel("For environment parameters and algorithm settings. (Placeholder)")
        desc.setWordWrap(True)

        placeholder_button = QtWidgets.QPushButton("Run (placeholder)")

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(placeholder_button)
        layout.addStretch()

        return panel
    
    def _build_right_panel(self) -> QtWidgets.QWidget:
        panel = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(panel)
        layout.setSpacing(12)

        canvas = self._build_canvas_placeholder()
        plot = self._build_plot_placeholder()

        layout.addWidget(canvas, stretch=3)
        layout.addWidget(plot, stretch=2)

        return panel
        
    def _build_canvas_placeholder(self) -> QtWidgets.QWidget:
        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setMinimumHeight(400)

        layout = QtWidgets.QVBoxLayout(frame)

        title = QtWidgets.QLabel("Grid Canvas")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        desc = QtWidgets.QLabel("Here will display the gridworld, value heatmap, and policy arrows.")
        desc.setAlignment(QtCore.Qt.AlignCenter)
        desc.setWordWrap(True)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch()

        return frame

    def _build_plot_placeholder(self) -> QtWidgets.QWidget:
        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setMinimumHeight(220)

        layout = QtWidgets.QVBoxLayout(frame)

        title = QtWidgets.QLabel("Plot Area")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        desc = QtWidgets.QLabel("Here will display convergence curves, training curves, or other statistical information.")
        desc.setAlignment(QtCore.Qt.AlignCenter)
        desc.setWordWrap(True)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch()

        return frame