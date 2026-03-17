import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')

    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

AZURE_TENANT_ID = "f958e84a-92b8-439f-a62d-4f45996b6d07"

AZURE_REDIRECT_URI = "https://udacitycms-hsggc0fbb9cpfayv.centralus-01.azurewebsites.net/auth"
