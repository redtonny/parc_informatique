## Parc Informatique – Application Django

Cette application gère le parc informatique d’un établissement : équipements, tickets de support, interventions et achats.

### 1. Installation

- **Prérequis** : Python 3.11+, PostgreSQL, `pip`, `virtualenv` (recommandé).
- Cloner le projet puis, dans le dossier du projet :

```bash
python -m venv venv
venv\Scripts\activate  # sous Windows
pip install -r requirements.txt  # si disponible, sinon installer Django, psycopg2-binary, python-dotenv
```

### 2. Configuration

Créer un fichier `.env` à la racine du projet avec par exemple :

```bash
DJANGO_SECRET_KEY=remplace_moi_en_prod
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=parcinfo_db
DB_USER=parcinfo_user
DB_PASSWORD=mot_de_passe
DB_HOST=127.0.0.1
DB_PORT=5432
```

### 3. Base de données et superutilisateur

Appliquer les migrations et créer un compte admin :

```bash
python manage.py migrate
python manage.py createsuperuser
```

Le modèle utilisateur personnalisé se trouve dans l’app `utilisateurs` (`Utilisateur` avec un champ `role` : `utilisateur`, `technicien` ou `admin`).

### 4. Lancer le serveur

```bash
python manage.py runserver
```

Accès principaux :

- Connexion : `/accounts/login/`
- Dashboard : `/` (vue `dashboard`)
- Tickets : `/ticket/`
- Parc informatique (équipements) : `/parcinfo/equipements/`
- Interventions : `/interventions/interventions/`
- Achats :
  - Fournisseurs : `/achats/fournisseurs/`
  - Commandes : `/achats/commandes/`

### 5. Rôles et sécurité

- L’accès aux vues métier est protégé par `login_required`.
- Les tickets sont filtrés par rôle (`utilisateur`, `technicien`, `admin`).
- L’assignation de tickets est réservée aux techniciens et administrateurs.

