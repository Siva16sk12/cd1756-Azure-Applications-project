import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cms-secret-key-12345-very-long-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage2'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'ENTER_CONNECTION_STRING'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_YOUR_PASSWORD'

    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://{user}%40{server}:{password}@{server}:1433/{db}'
        '?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes'
    ).format(
        user=os.environ.get('SQL_USER_NAME', 'cmsadmin'),
        server=os.environ.get('SQL_SERVER', 'cms1.database.windows.net'),
        password=os.environ.get('SQL_PASSWORD', 'ENTER_YOUR_PASSWORD'),
        db=os.environ.get('SQL_DATABASE', 'cms')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'ENTER_CLIENT_SECRET_HERE'
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'ENTER_CLIENT_ID_HERE'
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
