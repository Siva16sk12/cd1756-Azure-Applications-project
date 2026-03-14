import os

# Database connection
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLAZURECONNSTR_DEFAULTCONNECTION",
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=PUT_YOUR_SQL_SERVER.database.windows.net;"
    "Database=cms;"
    "Uid=PUT_YOUR_SQL_USERNAME;"
    "Pwd=PUT_YOUR_SQL_PASSWORD;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask secret key
SECRET_KEY = os.getenv("SECRET_KEY", "this_is_my_secret_key")


# Azure Blob Storage
BLOB_ACCOUNT = os.getenv("BLOB_ACCOUNT", "PUT_YOUR_STORAGE_ACCOUNT_NAME")
BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY", "PUT_YOUR_STORAGE_KEY")
BLOB_CONTAINER = os.getenv("BLOB_CONTAINER", "images")


# Microsoft Login (Azure Entra ID)
AZURE_CLIENT_ID = "PUT_YOUR_CLIENT_ID"
AZURE_CLIENT_SECRET = "PUT_YOUR_CLIENT_SECRET"
AZURE_TENANT_ID = "PUT_YOUR_TENANT_ID"

AZURE_REDIRECT_URI = "https://udacitycms-hsggc0fbb9cpfayv.centralus-01.azurewebsites.net/auth"
