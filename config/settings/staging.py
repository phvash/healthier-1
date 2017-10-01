import os
import sys

from .local import *


DATABASES['default'] = env.db('CLEARDB_DATABASE_URL')

# try:

#     # Check to make sure DATABASES is set in settings.py file.
#     # If not default to {}

#     if 'DATABASES' not in locals():
#         DATABASES = {}

#     if 'DATABASE_URL' in os.environ:

#         # Ensure default database exists.
#         DATABASES['default'] = DATABASES.get('default', {})

#         # Update with environment configuration.
#         DATABASES['default'].update({
#             'NAME': os.environ.get('DB_NAME'),
#             'USER': os.environ.get('DB_USERNAME'),
#             'PASSWORD': os.environ.get('DB_PWD'),
#             'HOST': os.environ.get('DB_HOST'),
#         })


#         if url.scheme == 'mysql':
#             DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
# except Exception:
#     print('Unexpected error:', sys.exc_info())
