from PySide6 import QtWidgets


class ToolPanel(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)

        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._build_ui()
        self.reset_to_defaults()

    def _build_ui(self) -> None:
        root_layout = QtWidgets.QVBoxLayout(self)
        root_layout.setSpacing(12)

        title = QtWidgets.QLabel("Control Panel")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        form = QtWidgets.QFormLayout()

        self.rows_spin = QtWidgets.QSpinBox()
        self.rows_spin.setRange(2, 50)
        self.rows_spin.setValue(5)

        self.cols_spin = QtWidgets.QSpinBox()
        self.cols_spin.setRange(2, 50)
        self.cols_spin.setValue(5)

        self.gamma_spin = QtWidgets.QDoubleSpinBox()
        self.gamma_spin.setRange(0.0, 1.0)
        self.gamma_spin.setSingleStep(0.01)
        self.gamma_spin.setDecimals(2)
        self.gamma_spin.setValue(0.95)

        self.theta_spin = QtWidgets.QDoubleSpinBox()
        self.theta_spin.setRange(0.0001, 1.0)
        self.theta_spin.setDecimals(4)
        self.theta_spin.setSingleStep(0.0001)
        self.theta_spin.setValue(0.0001)

        self.play_speed_spin = QtWidgets.QDoubleSpinBox()
        self.play_speed_spin.setRange(0.1, 10.0)
        self.play_speed_spin.setDecimals(1)
        self.play_speed_spin.setSingleStep(0.1)
        self.play_speed_spin.setValue(1.0)

        self.max_iterations_spin = QtWidgets.QSpinBox()
        self.max_iterations_spin.setRange(1, 10000)
        self.max_iterations_spin.setValue(200)

        form.addRow("Rows", self.rows_spin)
        form.addRow("Cols", self.cols_spin)
        form.addRow("Gamma", self.gamma_spin)
        form.addRow("Theta", self.theta_spin)
        form.addRow("Play Speed", self.play_speed_spin)
        form.addRow("Max iterations", self.max_iterations_spin)

        self.run_button = QtWidgets.QPushButton("Run")
        self.reset_button = QtWidgets.QPushButton("Reset")

        button_row = QtWidgets.QHBoxLayout()
        button_row.addWidget(self.run_button)
        button_row.addWidget(self.reset_button)

        hint = QtWidgets.QLabel(
            "terminal states、obstacles、reward settings will be added in the future. "
        )
        hint.setWordWrap(True)
        hint.setStyleSheet("color: gray;")

        root_layout.addWidget(title)
        root_layout.addLayout(form)
        root_layout.addLayout(button_row)
        root_layout.addWidget(hint)
        root_layout.addStretch()

    def get_config(self) -> dict[str, int | float]:
        return {
            "rows": self.rows_spin.value(),
            "cols": self.cols_spin.value(),
            "gamma": self.gamma_spin.value(),
            "theta": self.theta_spin.value(),
            "play_speed": self.play_speed_spin.value(),
            "max_iterations": self.max_iterations_spin.value(),
        }
    
    def reset_to_defaults(self) -> None:
        self.rows_spin.setValue(5)
        self.cols_spin.setValue(5)
        self.gamma_spin.setValue(0.95)
        self.theta_spin.setValue(0.0001)
        self.play_speed_spin.setValue(1.0)
        self.max_iterations_spin.setValue(200)