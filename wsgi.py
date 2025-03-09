import os
from app import create_app

# Erstelle die Anwendungsinstanz mit der Standardkonfiguration oder
# der Konfiguration aus der Umgebungsvariable
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 