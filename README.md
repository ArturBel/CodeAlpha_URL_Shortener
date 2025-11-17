# Simple URL Shortener

## Description
Simple URL Shortener, which allows users to shorten long URL. This repository is part of [Backend Development Projects](https://roadmap.sh/projects/url-shortening-service) on roadmap.sh.

---
## Project structure
```
URL_Shortener/
├── api/
│   ├── static
|   |   └── style.css     # css design for template
│   ├── templates
|   |   └── index.html    # html template for index page
|   ├── __init__.py       # flask's app initialization
│   ├── config.py         # app's configuration
│   ├── extensions.py     # extensions for app
│   ├── models.py         # model for database 
│   ├── routes.py         # routes supported by app
|   └── scheduler.py      # scheduler settings
├── migrations/           # alembic output (used for db migration and upgrade)
├── .env                  # secrets are stored here
├── .env.example          # example of how .env should look like
├── .gitignore            # gitignore file to not commit files
├── app.py                # flask's app instance (and run script)
└── requirements.txt      # requirements for project
```

---
## Main features
- Friendly user interface (front-end)
- URL validation
- Unique short URLs
- Error handling
- Deletion of unused URLs
---
## Installation
1) Clone the repository:
```
> git clone https://github.com/ArturBel/URL_Shortener.git
> cd URL_Shortener
```

2) Create and activate virtual environment:
```
> python -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
```

3) Create database in Postgres for storage (and/or testing) and apply migration.
```
psql> CREATE DATABASE url_shortener OWNER postgres;       # main db
> flask db upgrade                   # migration files are already created
```

4) Create .env file to store secrets, paste there example file and add real values:
```
.env   # your .env might look like this

DATABASE_URL=postgresql://postgres:password@localhost:5432/url-shortener
SECRET_KEY=re3G67fFb7T
HOST=localhost
PORT=5000
RATELIMIT_STORAGE_URI=redis://localhost:6379
REFRESH_HOURS=24
```

4) Run Flask app:
```
> python app.py
# or manually run app.py script
```

---
## Author

Artur Belotserkovskiy
- Github: https://github.com/ArturBel
- LinkedIn: https://www.linkedin.com/in/artur-belotserkovskiy-346135274/
