- Each django model is a class that subclasses django.db.models.Model
- each attribute of the model represents a database field
    - each field is specified as a class attribute; which maps to a DB column

To publish the models, add the package containing the model to INSTALL_APPS;
then run ```manage.py syncdb```.

cascade on delete is the default for foreign keys.
