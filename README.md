# Personal Website
Personal website generated with Django. Website includes a loading page, recipe portfolio, music/movies/book dashboards, personal finance (PF) summarization graphs, PF web API + documents, food prediction ML classification bot.

## App Maintenance 
### Recipes
#### Recipe and image additions
1. Crop, rename, and compress image to appropriate square. Save to `./media/recipes`.
2. Add recipe through admin panel with appropriate fields filled.
3. Push new images to Heroku.

#### Recipes database changes
1. `python manage.py makemigrations`
2. `python manage.py migrate`
- To reset heroku db: `heroku pg:reset <remote heroku db name>`
- To push local db to heroku: `heroku pg:push <local db name> <remote heroku db name> --app <heroku app name>`, ensure environment variables PGUSER, PGPASSWORD are correct [defunc]
- To pull heroku db to local: `heroku pg:pull <remote heroku db name> <local db name> --app <heroku app name>`, delete local db if exists
- To create users to heroku's db: `heroku run python manage.py createsuperuser`

### Music/Books & Movies:
(this does not need to be reguarly updated)
1. Update interests.db through `../Preprocessing/Interests Analysis/create_interests_db.py`
2. Save new interests.db in `./media`

### API:
(this does not need to be reguarly updated)
1. Update account_data.db and monthly_summary.db and scrub through `../Preprocessing/PF/scrub_databases.py`
2. Save databases into `./api/dbs/`

### PF (API doc):
(update only when API changes)
1. `python manage.py spectacular --file pf/templates/schema.yml`
2. Upload to editor.swagger.io
3. Generate html2 file and save to `./pf/templates/api_doc.html`

### Pushing to Heroku
1) `python manage.py collectstatic`
2) `git add .`
3) `git commit -m <message>`
4) `git push heroku master`

### Run website with Docker:
1. Ensure docker-compose.yaml is up-to-date
    - .env file includes:
        - `SECRET_KEY_mysite_new=<VAL>`
        - `run_heroku=<BOOL>`
        - `run_docker=<BOOL>`
    - recipes_db (postgres db) includes:
        - `POSTGRES_DB=cookings_db`
        - `POSTGRES_USER=postgres`
        - `POSTGRES_PASSWORD=postgres`
2. Clone repo to local directory
3. `docker-compose -f docker-compose.yaml up`
