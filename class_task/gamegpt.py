import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
class DataDetectiveApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Data Detective'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a central widget and set layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Data Display
        self.label = QLabel('Enter your hypothesis on why sales are decreasing:', self)
        self.line_edit = QLineEdit(self)
        self.check_button = QPushButton('Check Hypothesis', self)
        self.check_button.clicked.connect(self.check_hypothesis)

        # Add matplotlib canvas
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)
        self.plot_sales_data()

        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.check_button)
        
        self.central_widget.setLayout(layout)

    def plot_sales_data(self):
        data = {
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Sales": [2000, 1800, 1500, 1700, 1600, 1400],
            "Refunds": [100, 150, 200, 100, 150, 300]
        }
        df = pd.DataFrame(data)
        ax = self.canvas.figure.subplots()
        ax.plot(df['Month'], df['Sales'], label='Sales')
        ax.plot(df['Month'], df['Refunds'], label='Refunds', linestyle='--')
        ax.set_title('Sales and Refund Trends')
        ax.legend()

    def check_hypothesis(self):
        hypothesis = self.line_edit.text().lower()
        if 'refunds' in hypothesis:
            QMessageBox.information(self, 'Hypothesis Result', 'Correct! Refunds are increasing, which is contributing to the decrease in sales.')
        else:
            QMessageBox.warning(self, 'Hypothesis Result', 'Not quite! Try analyzing the data again.')

# Running the application
def main():
    app = QApplication(sys.argv)
    ex = DataDetectiveApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
