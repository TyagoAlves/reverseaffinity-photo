from PyQt5.QtGui import QPalette, QColor


DARK_THEME = """
QMainWindow, QDialog, QWidget {
    background-color: #1a1a2e;
    color: #e0e0e0;
    font-size: 12px;
}

QMenuBar {
    background-color: #0e0e1a;
    color: #c8c8c8;
    border-bottom: 1px solid #2a2a3e;
    padding: 2px 0;
    font-size: 12px;
}
QMenuBar::item {
    padding: 4px 12px;
    background: transparent;
}
QMenuBar::item:selected {
    background: #2a2a3e;
    color: #f0f0f0;
}
QMenuBar::item:pressed {
    background: #3a3a4e;
}
QMenu {
    background-color: #0e0e1a;
    border: 1px solid #333;
    padding: 4px 0;
}
QMenu::item {
    padding: 6px 36px 6px 14px;
}
QMenu::item:selected {
    background: #3a8ac4;
    color: #fff;
}
QMenu::separator {
    height: 1px;
    background: #333;
    margin: 4px 12px;
}
QMenu::right-arrow {
    image: none;
}
QMenu::indicator {
    width: 14px;
    height: 14px;
    margin-left: 8px;
}

QToolBar {
    background-color: #0e0e1a;
    border: none;
    border-bottom: 1px solid #2a2a3e;
    spacing: 2px;
    padding: 1px;
}
QToolBar::separator {
    width: 1px;
    background: #333;
    margin: 2px 3px;
}

QDockWidget {
    background-color: #0e0e1a;
    border: 1px solid #2a2a3e;
    titlebar-close-icon: none;
    titlebar-normal-icon: none;
}
QDockWidget::title {
    background-color: #1a1a2e;
    padding: 4px 8px;
    border-bottom: 1px solid #2a2a3e;
    color: #c0c0c0;
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

QPushButton {
    background-color: #2a2a3e;
    color: #d0d0d0;
    border: 1px solid #444;
    border-radius: 4px;
    padding: 4px 12px;
    min-height: 20px;
}
QPushButton:hover {
    background-color: #3a4a6e;
    border-color: #5a8ac4;
}
QPushButton:pressed {
    background-color: #3a8ac4;
    color: #fff;
}
QPushButton:disabled {
    background-color: #181828;
    color: #555;
    border-color: #282838;
}

QToolButton {
    background-color: transparent;
    color: #c0c0c0;
    border: 1px solid transparent;
    border-radius: 3px;
    padding: 2px 4px;
}
QToolButton:hover {
    background-color: #2a2a3e;
    border-color: #444;
}
QToolButton:checked {
    background-color: #3a8ac4;
    color: #fff;
    border-color: #5a9ad4;
}

QComboBox {
    background-color: #0e0e1a;
    color: #d0d0d0;
    border: 1px solid #333;
    border-radius: 4px;
    padding: 2px 6px;
    min-height: 20px;
}
QComboBox:hover {
    border-color: #555;
}
QComboBox::drop-down {
    border: none;
    width: 18px;
}
QComboBox QAbstractItemView {
    background-color: #0e0e1a;
    border: 1px solid #333;
    selection-background-color: #3a8ac4;
    selection-color: #fff;
    outline: none;
}

QSpinBox {
    background-color: #0e0e1a;
    color: #d0d0d0;
    border: 1px solid #333;
    border-radius: 4px;
    padding: 1px 4px;
    min-height: 18px;
}
QSpinBox:hover {
    border-color: #555;
}

QSlider::groove:horizontal {
    background: #1a1a2e;
    height: 4px;
    border-radius: 2px;
}
QSlider::handle:horizontal {
    background: #555;
    width: 12px;
    height: 12px;
    margin: -4px 0;
    border-radius: 6px;
}
QSlider::handle:horizontal:hover {
    background: #3a8ac4;
}
QSlider::sub-page:horizontal {
    background: #3a8ac4;
    border-radius: 2px;
}

QScrollBar:vertical {
    background: #0a0a18;
    width: 8px;
    border: none;
}
QScrollBar::handle:vertical {
    background: #333;
    min-height: 30px;
    border-radius: 4px;
}
QScrollBar::handle:vertical:hover {
    background: #555;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
    border: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:horizontal {
    background: #0a0a18;
    height: 8px;
    border: none;
}
QScrollBar::handle:horizontal {
    background: #333;
    min-width: 30px;
    border-radius: 4px;
}
QScrollBar::handle:horizontal:hover {
    background: #555;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
    border: none;
}

QListWidget {
    background-color: #0e0e1a;
    border: 1px solid #333;
    border-radius: 4px;
    outline: none;
    padding: 2px;
}
QListWidget::item {
    padding: 4px 8px;
    border-radius: 2px;
    color: #c0c0c0;
}
QListWidget::item:selected {
    background-color: #3a8ac4;
    color: #fff;
}
QListWidget::item:hover:!selected {
    background-color: #1a1a2e;
}

QStatusBar {
    background-color: #0e0e1a;
    border-top: 1px solid #2a2a3e;
    color: #999;
    font-size: 11px;
}
QStatusBar::item {
    border: none;
}

QLabel {
    color: #c0c0c0;
    background: transparent;
    font-size: 11px;
}
QLabel:disabled {
    color: #555;
}

QGroupBox {
    background-color: #0e0e1a;
    border: 1px solid #2a2a3e;
    border-radius: 4px;
    margin-top: 12px;
    font-weight: 600;
    padding: 10px 6px 6px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 1px 6px;
    color: #c0c0c0;
}

QLineEdit {
    background-color: #0e0e1a;
    color: #d0d0d0;
    border: 1px solid #333;
    border-radius: 4px;
    padding: 6px;
    min-height: 18px;
}
QLineEdit:focus {
    border-color: #3a8ac4;
}

QCheckBox {
    color: #c0c0c0;
    spacing: 4px;
}
QCheckBox::indicator {
    width: 14px;
    height: 14px;
    border: 1px solid #444;
    border-radius: 2px;
    background: #0e0e1a;
}
QCheckBox::indicator:checked {
    background: #3a8ac4;
    border-color: #3a8ac4;
}

QSplitter::handle {
    background: #1a1a2e;
    width: 1px;
}

QTabWidget::pane {
    background-color: #0e0e1a;
    border: none;
    border-top: 1px solid #2a2a3e;
}
QTabBar::tab {
    background-color: #0a0a18;
    color: #888;
    border: none;
    border-bottom: 2px solid transparent;
    padding: 5px 12px;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}
QTabBar::tab:selected {
    background-color: #0e0e1a;
    color: #e0e0e0;
    border-bottom: 2px solid #3a8ac4;
}
QTabBar::tab:hover:!selected {
    background-color: #1a1a2e;
    color: #aaa;
}

QProgressBar {
    background-color: #0e0e1a;
    border: none;
    border-radius: 2px;
    text-align: center;
    color: #c0c0c0;
    height: 12px;
}
QProgressBar::chunk {
    background-color: #3a8ac4;
    border-radius: 2px;
}
"""


def apply_dark_theme(app):
    app.setStyleSheet(DARK_THEME)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(26, 26, 46))
    palette.setColor(QPalette.WindowText, QColor(224, 224, 224))
    palette.setColor(QPalette.Base, QColor(14, 14, 26))
    palette.setColor(QPalette.AlternateBase, QColor(26, 26, 46))
    palette.setColor(QPalette.ToolTipBase, QColor(26, 26, 46))
    palette.setColor(QPalette.ToolTipText, QColor(224, 224, 224))
    palette.setColor(QPalette.Text, QColor(208, 208, 208))
    palette.setColor(QPalette.Button, QColor(42, 42, 62))
    palette.setColor(QPalette.ButtonText, QColor(208, 208, 208))
    palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
    palette.setColor(QPalette.Highlight, QColor(58, 138, 196))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    app.setPalette(palette)


APP_ICONS = {
    "photo": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
<rect x="4" y="8" width="40" height="32" rx="2" fill="#3a8ac4"/>
<circle cx="16" cy="20" r="5" fill="#fff"/>
<path d="M4 40l12-16 8 10 6-8 14 14H4z" fill="#2a6a94"/>
</svg>""",
    "video": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
<rect x="2" y="10" width="32" height="28" rx="3" fill="#3a8a3a"/>
<path d="M34 18l12 7-12 7V18z" fill="#5aaa5a"/>
<circle cx="12" cy="20" r="4" fill="#fff" opacity=".6"/>
</svg>""",
}


def get_app_icon(mode="photo"):
    from PyQt5.QtGui import QIcon, QPixmap
    from PyQt5.QtSvg import QSvgRenderer
    from PyQt5.QtCore import QByteArray, QRect
    svg_data = APP_ICONS.get(mode, APP_ICONS["photo"])
    renderer = QSvgRenderer(QByteArray(svg_data.encode()))
    pixmap = QPixmap(48, 48)
    pixmap.fill(Qt.transparent)
    from PyQt5.QtGui import QPainter
    p = QPainter(pixmap)
    renderer.render(p, QRect(0, 0, 48, 48))
    p.end()
    return QIcon(pixmap)
