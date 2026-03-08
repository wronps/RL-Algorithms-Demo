from PySide6 import QtCore, QtWidgets


class GridCanvas(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)

        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setMinimumHeight(400)

        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        title = QtWidgets.QLabel("Grid Canvas")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        desc = QtWidgets.QLabel(
            "Here will display the gridworld, value heatmap, and policy arrows."
        )
        desc.setAlignment(QtCore.Qt.AlignCenter)
        desc.setWordWrap(True)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch()