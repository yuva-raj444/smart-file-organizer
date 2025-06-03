import sys
from PyQt5.QtWidgets import QApplication
from ui import FileOrganizer
from constants import BASE_DIR
from PyQt5.QtGui import QIcon
import os

if __name__ == '__main__':
    app = QApplication(sys.argv)

    icon_path = os.path.join(BASE_DIR, "resources/logo.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    organizer = FileOrganizer()
    organizer.show()
    sys.exit(app.exec_())
