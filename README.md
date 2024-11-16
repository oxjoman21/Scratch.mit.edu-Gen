# Erstelle ein neues Verzeichnis für dein Projekt und navigiere hinein
mkdir mein-projekt
cd mein-projekt

# Erstelle die README.md mit Platzhaltern und öffne sie zum Bearbeiten
echo # Mein Projekt > README.md
echo. >> README.md
echo ## Projektbeschreibung >> README.md
echo *Kurze Beschreibung des Projekts.* >> README.md
echo. >> README.md
echo ## Installation >> README.md
echo *Schritte zur Installation des Projekts.* >> README.md
echo ```bash >> README.md
echo # Beispiel für eine Installation >> README.md
echo git clone https://github.com/benutzername/mein-projekt.git >> README.md
echo cd mein-projekt >> README.md
echo ``` >> README.md
echo. >> README.md
echo ## Verwendung >> README.md
echo *Anweisungen zur Verwendung des Projekts.* >> README.md
echo ```bash >> README.md
echo # Beispielbefehl >> README.md
echo node index.js >> README.md
echo ``` >> README.md
echo. >> README.md
echo ## Beitragende >> README.md
echo - Benutzername1 >> README.md
echo - Benutzername2 >> README.md
echo. >> README.md
echo ## Lizenz >> README.md
echo *Informationen zur Projektlizenz, falls zutreffend.* >> README.md

# Initialisiere ein Git-Repository und füge die README.md hinzu
git init
git add README.md
git commit -m "Initialisiere Repository mit Platzhalter-README"

# Optional: Verbinde das lokale Repository mit GitHub (ersetze die URL mit deiner eigenen)
git remote add origin https://github.com/benutzername/mein-projekt.git
git push -u origin main
