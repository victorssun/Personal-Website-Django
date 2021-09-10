# Personal Website
Personal website generated with Django. Website includes a loading page, recipe portfolio, music/movies/book dashboards, personal finance (PF) summarization graphs, PF web API + documents, food prediction ML classification bot.

## App Maintenance Procedure
Recipes:
```
1) Crop, rename, and compress image to appropriate square. Save to ./media/recipes
2) Add recipe through admin panel with appropriate name
3) Push new images to Heroku
```

Music/Books & Movies:
(this does not need to be reguarly updated)
```
1) Update interests.db through ../Preprocessing/Interests Analysis/create_interests_db.py
2) Save new interests.db in ./media
```

API:
(this does not need to be reguarly updated)
```
1) Update account_data.db and monthly_summary.db and scrub through ../Preprocessing/PF/scrub_databases.py
2) Save databases into ./api/dbs/
```

PF (API doc):
(update only when API changes)
```
1) python manage.py spectacular --file pf/templates/schema.yml
2) Upload to editor.swagger.io
3) Generate html2 file and save to ./pf/templates/api_doc.html
```

Recipes database changes:
```
1) python manage.py makemigrations
2) python manage.py migrate
- to reset heroku db: heroku pg:reset <remote heroku db name>
- to push local db to heroku: heroku pg:push <local db name> <remote heroku db name> --app <heroku app name>, ensure environment variables PGUSER, PGPASSWORD are correct [doesn't seem to work]
- to pull heroku db to local: heroku pg:pull <remote heroku db name> <local db name> --app <heroku app name>, delete local db if exists
- to create users to heroku's db: heroku run python manage.py createsuperuser
```

Pushing to Heroku
```
1) python manage.py collectstatic
2) git add .
3) git commit -m <message>
4) git push heroku master
```