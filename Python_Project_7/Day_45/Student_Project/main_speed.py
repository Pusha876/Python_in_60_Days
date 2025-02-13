from PyQt6.QtWidgets import QApplication, QWidget, QLabel, \
    QGridLayout, QLineEdit, QPushButton, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Imperial (miles)', 'Metric (km)'])

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.result_label = QLabel("")

        # Add widgets to grid Layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        # Get distance and time from the input boxes
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        # Calculate average speed
        speed = distance/time

        # Check what user choose in the combo box
        if self.combo.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'
        if self.combo.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            unit = 'km/h'

        # Display the result
        self.result_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
# The snippet above is a simple speed calculator that calculates speed
# based on distance and time.
