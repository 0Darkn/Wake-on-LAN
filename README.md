## Versão em Qt (PyQt5) – Wake-on-LAN

## Como correr o script

### ✅ 1. Instalar dependências

No terminal / CMD / PowerShell:

```bash
pip install PyQt5 wakeonlan
```

Se usares Python 3.11+ e der erro:

```bash
python -m pip install PyQt5 wakeonlan
```

---

### ✅ 2. Guardar o ficheiro

Exemplo:

```
wake_on_lan_qt.py
```

---

### ✅ 3. Executar o programa

#### Windows

```bash
python wake_on_lan_qt.py
```

#### Linux / macOS

```bash
python3 wake_on_lan_qt.py
```

---

## 4️⃣ Requisitos para o Wake-on-LAN funcionar

No **PC remoto**:

✔ Wake-on-LAN ativado na BIOS/UEFI
✔ Placa de rede configurada para WOL
✔ PC ligado à corrente (não desligado da tomada)
✔ Normalmente funciona melhor na **mesma rede local**

---

## 5️⃣ Próximas melhorias possíveis 🚀

Adicionar:

* ✔ Lista de PCs guardada em XML/JSON
* ✔ Histórico / log de envios
* ✔ Botão “Testar MAC”
* ✔ Broadcast configurável
* ✔ Versão PySide6
* ✔ Empacotar em `.exe` (PyInstaller)

