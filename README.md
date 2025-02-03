# Discord Server Backup & Restore Bot

Ein **Python-Bot**, der automatisch ein Backup eines Discord-Servers erstellt und eine Wiederherstellung aus einem gespeicherten Backup ermöglicht.  
Er speichert **Kanäle, Rollen, Berechtigungen und Emojis** als JSON-Datei und kann diese auch wiederherstellen.

## 📌 Features
✅ Speichert **alle Kanäle** (Text, Voice, Kategorien)  
✅ Speichert **alle Rollen** inklusive **Berechtigungen**  
✅ Speichert **kanalspezifische Berechtigungen** für jede Rolle  
✅ Speichert **Emojis & Sticker**  
✅ **Wiederherstellung** von Kanälen, Rollen & Berechtigungen aus dem Backup  
✅ Export als **JSON-Datei**  

## 📋 Installation & Nutzung

### 1️⃣ Voraussetzungen
1. Installiere **Python** (falls nicht vorhanden)  
2. Installiere `discord.py`:
   ```bash
   pip install discord.py
   ```
3. Erstelle einen Discord-Bot:
   - Gehe zu [Discord Developer Portal](https://discord.com/developers/applications)
   - Erstelle eine neue Anwendung und füge einen **Bot** hinzu
   - Aktiviere **"Server Members Intent"**  
   - Kopiere den **Bot-Token**  

4. Lade den Bot mit folgendem Link auf deinen Server ein:
   ```
   https://discord.com/oauth2/authorize?client_id=BOT_ID&scope=bot&permissions=8
   ```

### 2️⃣ Nutzung: Backup erstellen
1. **Ersetze** `DEIN_BOT_TOKEN_HIER` in `Restore.py` mit deinem Token.  
2. **Starte den Bot**, um ein Backup zu erstellen:
   ```bash
   python Restore.py
   ```
3. Der Bot speichert das Backup als **JSON-Datei** im gleichen Ordner.

### 3️⃣ Nutzung: Wiederherstellen des Servers
1. Stelle sicher, dass du eine gültige **Backup-Datei** hast (z. B. `discord_backup.json`).  
2. Entferne das `#` vor `await restore_guild(guild)` in `Restore.py`, um die Wiederherstellung zu aktivieren.  
3. **Starte den Bot erneut**, um den Server wiederherzustellen:
   ```bash
   python Restore.py
   ```

## ⚠️ Einschränkungen
❌ **Nachrichten** können nicht gespeichert werden (Discord API erlaubt das nicht)  
❌ **Voice-Chats & Direktnachrichten** werden nicht gesichert  
❌ **Bots & deren Einstellungen** müssen manuell gesichert werden  

## 🔄 Zukünftige Verbesserungen
- 🔹 **Automatische Wiederherstellung** ohne Code-Änderung  
- 🔹 **Backup für Nachrichten (lokal, falls erlaubt)**  
- 🔹 **Optionale GUI für einfachere Nutzung**  

---

### 📧 Support
Falls du Fragen hast oder Hilfe benötigst, erstelle ein Issue oder kontaktiere mich.  
Viel Spaß mit deinem **Discord Backup & Restore Bot**! 😊
