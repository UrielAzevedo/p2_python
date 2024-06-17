import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFileDialog, QTableView, QWidget, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

class TemperaturesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.data = None
        
        self.setWindowTitle("Graficos Dados de Temperatura")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        
        self.load_button = QPushButton("Carregar CSV")
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)
        
        self.table_view = QTableView()
        self.layout.addWidget(self.table_view)
        
        self.button_layout = QHBoxLayout()
        
        self.plot_cartesian_button = QPushButton("Plotar Gráfico Cartesiano")
        self.plot_cartesian_button.clicked.connect(self.plot_cartesian)
        self.button_layout.addWidget(self.plot_cartesian_button)
        
        self.plot_bar_button = QPushButton("Plotar Gráfico de Barras")
        self.plot_bar_button.clicked.connect(self.plot_bar)
        self.button_layout.addWidget(self.plot_bar_button)
        
        self.layout.addLayout(self.button_layout)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    
    def load_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.data = pd.read_csv(file_path)
            self.display_data()
    
    def display_data(self):
        if self.data is not None:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.data.columns.tolist())
            
            for row in self.data.itertuples(index=False):
                items = [QStandardItem(str(item)) for item in row]
                model.appendRow(items)
            
            self.table_view.setModel(model)
            self.table_view.resizeColumnsToContents()

    def plot_cartesian(self):
        if self.data is not None:
            data_t = self.data.T
            data_t.plot()
            plt.title('Gráfico Cartesiano')
            plt.xlabel('Meses')
            plt.ylabel('Temperatura')
            plt.show()
    
    def plot_bar(self):
        if self.data is not None:
            data_t = self.data.T
            data_t.plot(kind='bar')
            plt.title('Gráfico de Barras')
            plt.xlabel('Meses')
            plt.ylabel('Temperatura')
            plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperaturesApp()
    window.show()
    sys.exit(app.exec_())
