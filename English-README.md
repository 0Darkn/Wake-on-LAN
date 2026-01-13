## Qt Version (PyQt5) – Wake-on-LAN

## How to run the script

### ✅ 1. Install dependencies

In Terminal / CMD / PowerShell:

```bash
pip install PyQt5 wakeonlan
```

If you are using Python 3.11+ and get an error:

```bash
python -m pip install PyQt5 wakeonlan
```

---

### ✅ 2. Save the file

Example:

```
wake_on_lan_qt.py
```

---

### ✅ 3. Run the program

#### Windows

```bash
python wake_on_lan_qt.py
```

#### Linux / macOS

```bash
python3 wake_on_lan_qt.py
```

---

## 4️⃣ Requirements for Wake-on-LAN to work

On the **remote PC**:

* ✔ Wake-on-LAN enabled in the BIOS/UEFI
* ✔ Network adapter configured for WOL
* ✔ PC connected to power (not unplugged)
* ✔ Usually works best on the **same local network**

---

## 5️⃣ Possible future improvements 🚀

Add:

* ✔ List of PCs stored in XML/JSON
* ✔ Send history / logs
* ✔ “Test MAC” button
* ✔ Configurable broadcast address
* ✔ PySide6 version
* ✔ Package as `.exe` (PyInstaller)

---
