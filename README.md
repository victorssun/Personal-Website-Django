# Personal Website
Personal website generated with Django. Website includes a loading page, recipe portfolio, music/movies/book dashboards, personal finance (PF) summarization graphs, PF web API + documents, food prediction ML classification bot.

## App Maintenance 
### Recipes
#### Recipe and image additions
1. Crop, rename, and compress image to appropriate square. Save to `./media/recipes`
2. Add recipe through admin panel with appropriate fields filled
3. Push changes to Heroku

#### Recipes database changes
1. `python manage.py makemigrations`
2. `python manage.py migrate`
- To reset heroku db: `heroku pg:reset <remote heroku db name>`
- To push local db to heroku: `heroku pg:push <local db name> <remote heroku db name> --app <heroku app name>`, ensure environment variables PGUSER, PGPASSWORD are correct [defunc]
- To pull heroku db to local: `heroku pg:pull <remote heroku db name> <local db name> --app <heroku app name>`, delete local db first if exists
- To create users to heroku's db: `heroku run python manage.py createsuperuser`
- If above does not work, below must be in run in bash (not PS):
    - To pull heroku db to local `https://stackoverflow.com/questions/65662333/heroku-pull-postgres-database-to-local-failed-with-unrecognized-data-block-type`: 
        - `heroku pg:backups:capture -a <app_name>`
        - `heroku pg:backups:download -a <app_name>` -- will save `latest.dump` file in current directory
        - `createdb -U postgres <db name>`
        - `pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d <local db name> latest.dump`
    - To push local db to heroku `https://gist.github.com/michaeltreat/c04e69ebd7a85eee15a29c8ea19c8d44`:
       - `pg_dump -U postgres -F c -c -O <local db name> > out.sql`
       - Go to heroku database credentials and grab user, pw, db, host
       - `PGUSER=<user> PGPASSWORD=<pass> pg_restore -h '<host>' -d <db> < out.sql`


#### Interactive recipe shell (local/heroku)
1. `python manage.py shell` / `heroku run python manage.py shell --app=<app_name>`
2. `from recipes.models import Recipe`
3. `from recipes.views import *`

#### Import recipes.xlsx file to database
1. Make <database_name> in Postgres
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py shell` / `heroku run python manage.py shell --app=<app_name>`
5. `from recipes.import_xlsx import *` with appropriate .xlsx path

### Music/Books & Movies:
(this does not need to be reguarly updated)
1. Update interests.db through `../Preprocessing/Interests Analysis/create_interests_db.py`
2. Save new interests.db in `./media`

### API:
(this does not need to be reguarly updated)
1. Update questrade.db and monthly_summary.db and scrub through `../Preprocessing/PF/scrub_databases.py`
2. Save databases into `./media/api_dbs/`

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
3. `docker-compose -f docker-compose.yaml up` (ensure Docker is on)
