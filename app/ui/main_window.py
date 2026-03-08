from PySide6 import QtCore, QtWidgets, QtGui
from app.ui.widgets.tool_panel import ToolPanel
from app.ui.widgets.grid_canvas import GridCanvas
from app.ui.widgets.plot_panel import PlotPanel
from core.mdp.gridworld import Gridworld

debug = 1

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RL Algorithms Demo")
        self.resize(1200, 900)

        self.menubar = self.menuBar()
        file_menu = self.menubar.addMenu("File")
        exit_action = QtGui.QAction("Exit", self)
        exit_action.setShortcut(QtGui.QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        self._build_ui()

    def _build_ui(self) -> None:
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        root_layout = QtWidgets.QHBoxLayout(central)
        root_layout.setContentsMargins(12, 12, 12, 12)
        root_layout.setSpacing(12)

        self.tool_panel = ToolPanel()
        right_panel = self._build_right_panel()

        self.tool_panel.setFixedWidth(300)
        root_layout.addWidget(self.tool_panel)
        root_layout.addWidget(right_panel, stretch=1)

        self.tool_panel.run_button.clicked.connect(self._handle_run_clicked)
        self.tool_panel.reset_button.clicked.connect(self._handle_reset_clicked)
        self.statusBar().showMessage("Ready")


 
    def _build_right_panel(self) -> QtWidgets.QWidget:
        panel = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(panel)
        layout.setSpacing(12)

        canvas = GridCanvas()
        plot = PlotPanel()

        layout.addWidget(canvas, stretch=3)
        layout.addWidget(plot, stretch=2)

        return panel
    
    def _handle_run_clicked(self) -> None:
        env_config = self.tool_panel.get_environment_config()
        alg_config = self.tool_panel.get_algorithm_config()
        play_speed = self.tool_panel.get_play_speed()
        try:
            env = Gridworld(env_config)
        except ValueError as exc:
            self.statusBar().showMessage(f"Invalid grid config: {exc}")
            return

        print("Environment config:", env_config)
        print("Environment object:", env)
        print("Algorithm config:", alg_config)
        print("Play speed:", play_speed)
        rows, cols = env.shape
        gamma = alg_config.gamma
        states = env.get_states()
        state_count = env.state_count
        actions = env.get_actions()
        print("States:", states)
        print("State count:", state_count)
        print("Actions:", actions)

        self.statusBar().showMessage(f"Run clicked | Grid: {rows}x{cols} | gamma={gamma} | step_reward={env.step_reward}")

    def _handle_reset_clicked(self) -> None:
        self.tool_panel.reset_to_defaults()
        self.statusBar().showMessage("Reset done")