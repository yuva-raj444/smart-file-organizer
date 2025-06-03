import ctypes
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout,
    QCheckBox, QScrollArea, QFrame, QGridLayout, QTextEdit
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QCursor, QIcon, QPixmap

from constants import FILE_CATEGORIES, BASE_DIR
from file_organizer import organize_files_in_folder


class FileOrganizer(QWidget):
    def __init__(self):
        super().__init__()

        # Taskbar Icon Fix (Windows only)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("SmartFileOrganizer")

        self.setWindowTitle("📁 Smart File Organizer")
        self.setGeometry(100, 50, 1200, 900)
        self.setStyleSheet("background-color: #1e1e2f; color: white; font-family: 'Segoe UI'; font-size: 28px;")
        self.setWindowIcon(QIcon(BASE_DIR + "/resources/logo.ico"))  # Icon for titlebar and .exe

        self.selected_folder = ""
        self.checkboxes = {}
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        logo_label = QLabel()
        logo_path = BASE_DIR + "/resources/logo.png"
        if logo_path:
            pixmap = QPixmap(logo_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                logo_label.setPixmap(scaled_pixmap)
                logo_label.setAlignment(Qt.AlignCenter)
                main_layout.addWidget(logo_label)

        self.label = QLabel("Select Folder to Organize")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 48px; padding: 20px; font-weight: bold;")
        main_layout.addWidget(self.label)

        self.browse_btn = QPushButton("Browse Folder")
        self.browse_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_btn.setStyleSheet(self.button_style(font_size="36px"))
        self.browse_btn.clicked.connect(self.select_folder)
        main_layout.addWidget(self.browse_btn)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        checkbox_container = QFrame()
        checkbox_layout = QGridLayout()
        num_columns = 3

        for i, (label_text, _) in enumerate(FILE_CATEGORIES.items()):
            checkbox = QCheckBox(label_text)
            checkbox.setStyleSheet("QCheckBox { spacing: 20px; padding: 10px; font-size: 30px; }")
            self.checkboxes[label_text] = checkbox
            checkbox_layout.addWidget(checkbox, i // num_columns, i % num_columns)

        checkbox_container.setLayout(checkbox_layout)
        scroll_area.setWidget(checkbox_container)
        main_layout.addWidget(scroll_area, stretch=4)

        self.organize_btn = QPushButton("✨ Organize Now")
        self.organize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.organize_btn.setStyleSheet(self.button_style(font_size="36px"))
        self.organize_btn.clicked.connect(self.organize_files)
        main_layout.addWidget(self.organize_btn)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("background-color: #2d2d3a; border-radius: 15px; padding: 20px; font-size: 30px;")
        main_layout.addWidget(self.result_box, stretch=3)

        self.setLayout(main_layout)
        self.add_hover_animation(self.browse_btn)
        self.add_hover_animation(self.organize_btn)

    def button_style(self, font_size="28px"):
        return (
            f"QPushButton {{ background-color: #3f51b5; color: white; border-radius: 15px; padding: 15px; font-size: {font_size}; }}"
            "QPushButton:hover { background-color: #5c6bc0; }"
        )

    def add_hover_animation(self, button):
        anim = QPropertyAnimation(button, b"pos")
        anim.setDuration(150)
        anim.setEasingCurve(QEasingCurve.OutQuad)

        def on_hover():
            anim.stop()
            anim.setStartValue(button.pos())
            anim.setEndValue(button.pos() + QPoint(0, -4))
            anim.start()

        def on_leave():
            anim.stop()
            anim.setStartValue(button.pos())
            anim.setEndValue(button.pos() + QPoint(0, 4))
            anim.start()

        button.enterEvent = lambda e: on_hover()
        button.leaveEvent = lambda e: on_leave()

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.selected_folder = folder
            self.label.setText(f"Selected: {folder}")

    def organize_files(self):
        if not self.selected_folder:
            self.result_box.setText("❗ Please select a folder first.")
            return

        selected_extensions = []
        label_map = {}
        for label_text, cb in self.checkboxes.items():
            if cb.isChecked():
                for ext in FILE_CATEGORIES[label_text]:
                    selected_extensions.append(ext)
                    label_map[ext] = label_text.split(" ")[0] + "s"

        if not selected_extensions:
            self.result_box.setText("❗ Please select at least one file type.")
            return

        moved_files = organize_files_in_folder(self.selected_folder, selected_extensions, label_map)

        if moved_files:
            summary = "✅ Files Organized:\n"
            for category, count in moved_files.items():
                summary += f"- {count} file(s) moved to {category}\n"
            self.result_box.setText(summary)
        else:
            self.result_box.setText("📁 No matching files found to organize.")
