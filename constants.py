import sys
import os

BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

FILE_CATEGORIES = {
    "PDF (.pdf)": [".pdf"],
    "Word (.doc, .docx)": [".doc", ".docx"],
    "Excel (.xls, .xlsx)": [".xls", ".xlsx"],
    "PowerPoint (.ppt, .pptx)": [".ppt", ".pptx"],
    "Text (.txt)": [".txt"],
    "Images (.jpg, .png)": [".jpg", ".jpeg", ".png"],
    "Videos (.mp4, .mkv)": [".mp4", ".mkv"],
    "Archives (.zip, .rar)": [".zip", ".rar"],
    "HTML/Web Files (.html, .css, .js)": [".html", ".htm", ".css", ".js"],
    "Audio Files (.mp3, .wav, .aac)": [".mp3", ".wav", ".aac", ".flac"],
    "Executables (.exe, .bat, .sh)": [".exe", ".bat", ".sh"],
    "CSV Files (.csv)": [".csv"],
    "JSON Files (.json)": [".json"],
    "Comprehensive Archives (.7z, .tar, .gz)": [".7z", ".tar", ".gz"],
    "CAD Files (.dwg, .dxf)": [".dwg", ".dxf"],
    "Database Files (.db, .sqlite, .mdb)": [".db", ".sqlite", ".mdb"],
    "Font Files (.ttf, .otf)": [".ttf", ".otf"],
    "Python Scripts (.py)": [".py", ".pyw"]
}
