import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox

class MySQLExporter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.exportButton = QPushButton('Export Data')
        self.exportButton.clicked.connect(self.exportData)

        layout.addWidget(self.exportButton)

        self.setLayout(layout)
        self.setWindowTitle('MySQL Data Exporter')
        self.setGeometry(300, 300, 300, 200)

    def exportData(self):
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
            host="localhost",
            user= "root",
            passwd= "password",
            database="ranil_proj")
    

            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")

            tables = cursor.fetchall()

            options = QFileDialog.Options()
            filePath, _ = QFileDialog.getSaveFileName(self, "Save SQL File", "", "SQL Files (*.sql);;All Files (*)", options=options)
            if filePath:
                with open(filePath, 'w') as f:
                    for table in tables:
                        table_name = table[0]
                        cursor.execute(f"SHOW CREATE TABLE {table_name}")
                        create_table_stmt = cursor.fetchone()[1]
                        f.write(f"{create_table_stmt};\n\n")

                        cursor.execute(f"SELECT * FROM {table_name}")
                        rows = cursor.fetchall()

                        if rows:
                            columns = [desc[0] for desc in cursor.description]
                            col_names = ", ".join(columns)
                            for row in rows:
                                values = ", ".join([f"'{str(val)}'" if val is not None else 'NULL' for val in row])
                                insert_stmt = f"INSERT INTO {table_name} ({col_names}) VALUES ({values});"
                                f.write(f"{insert_stmt}\n")
                            f.write("\n")
                        
                QMessageBox.information(self, "Success", "Data exported successfully!")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error: {err}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exporter = MySQLExporter()
    exporter.show()
    sys.exit(app.exec_())
