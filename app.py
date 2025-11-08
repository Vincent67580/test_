from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Page à propos
@app.route('/about')
def about():
    return render_template('about.html')


# Page projets
@app.route('/projets')
def projets():
    mes_projets = [
        {
            "image": url_for('static', filename='images/imageProjetPortfolio.png'),
            "titre": "Portfolio personnel", 
            "description": """Développement complet de mon <strong>site portfolio</strong> afin de présenter mes compétences, 
                mes projets et mon parcours professionnel.  
                Le site a été entièrement conçu en <strong>HTML</strong>, <strong>CSS</strong> et <strong>JavaScript</strong>, 
                avec une attention particulière portée à la <strong>structure sémantique</strong>, 
                la <strong>responsivité</strong> et l’<strong>esthétique</strong>."""
        },
        {
            "titre": "Application Python de gestion de rendez-vous", 
            "description": """Développement d’une application en <strong>Python</strong> fonctionnant en <strong>mode console</strong>, 
                    permettant de <strong>gérer des rendez-vous clients</strong> (ajout, affichage, modification, suppression) 
                    et d’envoyer automatiquement un <strong>e-mail de confirmation ou d’annulation</strong> à chaque action.
                    <ul class="tech-list">
                    <li>Langage : Python</li>
                    <li>Base de données : SQLite3</li>
                    <li>Modules : smtplib, email, sqlite3</li>
                    <li>Fonctionnalités : prise/suppression de RDV, validation, notifications automatiques</li>
                </ul>"""
        },
        {
            "titre": "Bot Python de recherche de restaurants", 
            "description": """<p>
                    Développement d’un <strong>bot console</strong> permettant de rechercher des 
                    <strong>restaurants autour d’une ville</strong> via les API 
                    <strong>OpenStreetMap (Nominatim & Overpass)</strong>.  
                    L’utilisateur choisit le <strong>rayon</strong>, le <strong>nombre de résultats</strong> 
                    et peut <strong>exporter la liste au format CSV</strong>.
                </p>

                <ul class="tech-list">
                    <li>Langage : Python</li>
                    <li>Bibliothèques : requests, json, csv, os</li>
                    <li>API utilisées : Nominatim (géolocalisation), Overpass (recherche OSM)</li>
                    <li>Fonctionnalités :
                    <ul>
                        <li>Recherche par ville et rayon personnalisé</li>
                        <li>Affichage des résultats avec adresse, type de cuisine, coordonnées GPS</li>
                        <li>Export automatique des données dans restaurants.csv</li>
                    </ul>
                    </li>
                </ul>"""
        },
    ]
    return render_template('projets.html', projets=mes_projets)

# Page contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        message = request.form['message']
        print(f"Nouveau message de {nom} ({email}) : {message}")  # Exemple simple
        return redirect(url_for('home'))
    return render_template('contact.html')





if __name__ == '__main__':
    # Récupère le port donné par Render (ou 5000 par défaut en local)
    port = int(os.environ.get("PORT", 5000))
    # Expose le serveur sur toutes les interfaces (obligatoire sur Render)
    app.run(host="0.0.0.0", port=port)
