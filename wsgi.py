import os
from simple_app import app

# Hier ist keine create_app-Funktion nötig, da simple_app.py die App-Instanz direkt definiert
# Wir müssen die app nur importieren

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 