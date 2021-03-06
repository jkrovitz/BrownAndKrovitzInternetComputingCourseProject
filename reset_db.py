'''
This file handles resetting the database. 

'''

from taskViz.models import db

print('Resetting database...')

# Reset the database
db.drop_all()
# Create the tables
db.create_all()
print('Database reset: success!')
