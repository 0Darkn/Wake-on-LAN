# pip install PyQt5 wakeonlan

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QAction
)
from wakeonlan import send_magic_packet


class WakeOnLanApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wake-on-LAN")
        self.setGeometry(300, 200, 400, 220)

        self._criar_menu()
        self._criar_interface()

    # -----------------------------
    # MENU
    # -----------------------------
    def _criar_menu(self):
        menu_bar = self.menuBar()

        menu_ficheiro = menu_bar.addMenu("Ficheiro")

        acao_sair = QAction("Sair", self)
        acao_sair.triggered.connect(self.close)

        menu_ficheiro.addAction(acao_sair)

    # -----------------------------
    # INTERFACE PRINCIPAL
    # -----------------------------
    def _criar_interface(self):
        widget_central = QWidget()
        layout = QVBoxLayout()

        # IP (opcional)
        label_ip = QLabel("Endereço IP (opcional):")
        self.entry_ip = QLineEdit()
        self.entry_ip.setPlaceholderText("Ex: 192.168.1.100")

        # MAC
        label_mac = QLabel("Endereço MAC:")
        self.entry_mac = QLineEdit()
        self.entry_mac.setPlaceholderText("Ex: AA:BB:CC:DD:EE:FF")

        # Botões
        botao_ligar = QPushButton("Ligar PC Remoto")
        botao_ligar.clicked.connect(self.ligar_pc_remoto)

        botao_sair = QPushButton("Sair")
        botao_sair.clicked.connect(self.close)

        # Adicionar ao layout
        layout.addWidget(label_ip)
        layout.addWidget(self.entry_ip)
        layout.addWidget(label_mac)
        layout.addWidget(self.entry_mac)
        layout.addWidget(botao_ligar)
        layout.addWidget(botao_sair)

        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    # -----------------------------
    # LÓGICA WAKE-ON-LAN
    # -----------------------------
    def ligar_pc_remoto(self):
        ip = self.entry_ip.text()   # Não usado diretamente
        mac = self.entry_mac.text()

        if not mac:
            QMessageBox.warning(self, "Atenção", "Por favor, insira um endereço MAC.")
            return

        try:
            send_magic_packet(mac)
            QMessageBox.information(
                self,
                "Sucesso",
                "Pacote Wake-on-LAN enviado com sucesso!"
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Erro",
                f"Erro ao enviar o pacote:\n{e}"
            )


# -----------------------------
# MAIN
# -----------------------------
def main():
    app = QApplication(sys.argv)
    janela = WakeOnLanApp()
    janela.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
