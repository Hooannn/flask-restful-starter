With the above application you can create a migration repository with the following command:

$ flask db init

This will add a migrations folder to your application. The contents of this folder need to be added to version control along with your other source files.

You can then generate an initial migration:

$ flask db migrate -m "Initial migration."

The migration script needs to be reviewed and edited, as Alembic is not always able to detect every change you make to your models. In particular, Alembic is currently unable to detect table name changes, column name changes, or anonymously named constraints. A detailed summary of limitations can be found in the Alembic autogenerate documentation. Once finalized, the migration script also needs to be added to version control.

Then you can apply the changes described by the migration script to your database:

$ flask db upgrade

Each time the database models change, repeat the migrate and upgrade commands.

To sync the database in another system just refresh the migrations folder from source control and run the upgrade command.

To see all the commands that are available run this command:

$ flask db --help

Note that the application script must be set in the FLASK_APP environment variable for all the above commands to work, as required by the flask command.
