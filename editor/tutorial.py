from PyQt5.QtCore import Qt, QTimer, QSettings
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCheckBox, QWidget, QStackedWidget,
)

from .i18n import _

STEPS = [
    {
        "icon": "🎨",
        "title": _("Welcome to reverseaffinity Photo"),
        "subtitle": _("Seu editor de imagens profissional, gratuito e de código aberto"),
        "desc": _(
            "Com ferramentas avançadas de pintura, seleção, ajustes de cor, "
            "camadas, filtros e muito mais — tudo que você precisa para criar "
            "e editar imagens com qualidade profissional."
        ),
    },
    {
        "icon": "🖌️",
        "title": _("Ferramentas de Edição"),
        "subtitle": _("Tudo ao seu alcance"),
        "desc": _(
            "Pinceis personalizaveis, selecao precisa, texto, formas geometricas, "
            "ferramenta de clonagem, gradiente e非常多 mais. A barra de ferramentas "
            "a esquerda da acesso rapido a todas as ferramentas."
        ),
    },
    {
        "icon": "📑",
        "title": _("Camadas e Ajustes"),
        "subtitle": _("Edicao nao-destrutiva"),
        "desc": _(
            "Trabalhe com camadas, mascaras, modos de mesclagem e camadas de ajuste. "
            "O painel de camadas permite organizar, agrupar, duplicar e mesclar "
            "camadas com total flexibilidade."
        ),
    },
    {
        "icon": "✨",
        "title": _("Filtros e Efeitos"),
        "subtitle": _("Transforme suas imagens"),
        "desc": _(
            "Aplique filtros profissionais como desfoque, nitidez, deteccao de bordas, "
            "relevo e非常多 mais. A Galeria de Filtros oferece visualizacao em "
            "tempo real dos efeitos."
        ),
    },
    {
        "icon": "⌨️",
        "title": _("Atalhos Importantes"),
        "subtitle": _("Trabalhe mais rapido"),
        "desc": _(
            "Ctrl+N  Novo arquivo\n"
            "Ctrl+O  Abrir imagem\n"
            "Ctrl+S  Salvar\n"
            "Ctrl+Z  Desfazer\n"
            "Ctrl+Shift+Z  Refazer\n"
            "Ctrl++  Zoom in\n"
            "Ctrl+-  Zoom out\n"
            "B  Pincel  |  E  Borracha  |  M  Selecao  |  T  Texto"
        ),
    },
    {
        "icon": "🚀",
        "title": _("Pronto para Criar!"),
        "subtitle": _("Comece agora mesmo"),
        "desc": _(
            "Abra uma imagem existente ou crie um novo arquivo para comecar. "
            "Explore os menus, experimente as ferramentas e descubra todo o "
            "potencial do reverseaffinity Photo."
        ),
    },
]


class SlidePage(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: transparent;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 20)
        layout.setSpacing(8)

        icon_label = QLabel(data["icon"])
        icon_label.setAlignment(Qt.AlignCenter)
        font = icon_label.font()
        font.setPointSize(48)
        icon_label.setFont(font)
        icon_label.setFixedHeight(80)
        layout.addWidget(icon_label)

        title = QLabel(data["title"])
        title.setAlignment(Qt.AlignCenter)
        title.setWordWrap(True)
        ft = title.font()
        ft.setPointSize(18)
        ft.setBold(True)
        title.setFont(ft)
        title.setStyleSheet("color: #e0e0e0; padding: 4px 0;")
        layout.addWidget(title)

        subtitle = QLabel(data["subtitle"])
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setWordWrap(True)
        fs = subtitle.font()
        fs.setPointSize(12)
        subtitle.setFont(fs)
        subtitle.setStyleSheet("color: #888; padding: 0 0 12px 0;")
        layout.addWidget(subtitle)

        desc = QLabel(data["desc"])
        desc.setAlignment(Qt.AlignCenter)
        desc.setWordWrap(True)
        fd = desc.font()
        fd.setPointSize(11)
        desc.setFont(fd)
        desc.setStyleSheet("color: #b0b0b0; line-height: 1.6;")
        layout.addWidget(desc)

        layout.addStretch()


class WelcomeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(_("Welcome"))
        self.setFixedSize(520, 460)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.setStyleSheet("""
            WelcomeDialog {
                background-color: #1e1e1e;
                border: 1px solid #333;
                border-radius: 8px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background: #1e1e1e; border-radius: 8px;")
        layout.addWidget(self.stack)

        for s in STEPS:
            self.stack.addWidget(SlidePage(s))

        nav_layout = QHBoxLayout()
        nav_layout.setContentsMargins(16, 8, 16, 12)

        self.dont_show = QCheckBox(_("Nao mostrar novamente"))
        self.dont_show.setStyleSheet("""
            QCheckBox {
                color: #888;
                font-size: 11px;
                spacing: 6px;
            }
            QCheckBox::indicator {
                width: 14px;
                height: 14px;
                border: 1px solid #555;
                border-radius: 2px;
                background: #2a2a2a;
            }
            QCheckBox::indicator:checked {
                background: #3a6ea5;
                border-color: #3a6ea5;
            }
        """)
        nav_layout.addWidget(self.dont_show)

        nav_layout.addStretch()

        self.btn_prev = QPushButton(_("&Anterior"))
        self.btn_prev.setFixedSize(100, 30)
        self.btn_prev.setStyleSheet("""
            QPushButton {
                background: #2a2a2a; color: #b0b0b0;
                border: 1px solid #444; border-radius: 4px;
                font-size: 12px; padding: 4px 12px;
            }
            QPushButton:hover { background: #3a3a3a; color: #e0e0e0; }
        """)
        self.btn_prev.clicked.connect(self._prev)
        nav_layout.addWidget(self.btn_prev)

        self.page_label = QLabel()
        self.page_label.setAlignment(Qt.AlignCenter)
        self.page_label.setFixedWidth(60)
        self.page_label.setStyleSheet("color: #666; font-size: 11px;")
        nav_layout.addWidget(self.page_label)

        self.btn_next = QPushButton(_("&Proximo"))
        self.btn_next.setFixedSize(100, 30)
        self.btn_next.setStyleSheet("""
            QPushButton {
                background: #3a6ea5; color: #fff;
                border: none; border-radius: 4px;
                font-size: 12px; padding: 4px 12px;
            }
            QPushButton:hover { background: #4a7eb5; }
        """)
        self.btn_next.clicked.connect(self._on_next)
        nav_layout.addWidget(self.btn_next)

        self.btn_close = QPushButton(_("&Pular Tour"))
        self.btn_close.setFixedSize(100, 30)
        self.btn_close.setStyleSheet("""
            QPushButton {
                background: transparent; color: #666;
                border: 1px solid #444; border-radius: 4px;
                font-size: 11px; padding: 4px 12px;
            }
            QPushButton:hover { color: #b0b0b0; border-color: #666; }
        """)
        self.btn_close.clicked.connect(self._close)
        nav_layout.addWidget(self.btn_close)

        layout.addLayout(nav_layout)

        self._update_buttons()
        self._auto_timer = QTimer(self)
        self._auto_timer.timeout.connect(self._on_next)
        self._auto_timer.setSingleShot(True)
        self._auto_timer.start(6000)

    def _update_buttons(self):
        idx = self.stack.currentIndex()
        total = self.stack.count()
        self.page_label.setText(f"{idx + 1} / {total}")
        self.btn_prev.setEnabled(idx > 0)
        if idx == total - 1:
            self.btn_next.setText(_("&Concluir"))
        else:
            self.btn_next.setText(_("&Proximo"))
        self.btn_close.setVisible(idx < total - 1)

    def _on_next(self):
        self._auto_timer.stop()
        idx = self.stack.currentIndex()
        if idx == self.stack.count() - 1:
            self._close()
        else:
            self.stack.setCurrentIndex(idx + 1)
            self._update_buttons()
            self._auto_timer.start(6000)

    def _prev(self):
        self._auto_timer.stop()
        if self.stack.currentIndex() > 0:
            self.stack.setCurrentIndex(self.stack.currentIndex() - 1)
            self._update_buttons()
            self._auto_timer.start(6000)

    def _close(self):
        self._auto_timer.stop()
        if self.dont_show.isChecked():
            settings = QSettings()
            settings.setValue("welcome_shown", True)
        self.accept()


def show_welcome_if_needed(parent=None):
    settings = QSettings()
    if settings.value("welcome_shown", False, type=bool):
        return
    dialog = WelcomeDialog(parent)
    dialog.exec_()
