import os

# ---------------- DATABASE ----------------

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


# ---------------- FLASK SECRET ----------------

SECRET_KEY = os.getenv("SECRET_KEY", "this_is_my_secret_key")


# ---------------- AZURE BLOB STORAGE ----------------

BLOB_ACCOUNT = os.getenv("BLOB_ACCOUNT", "PUT_YOUR_STORAGE_ACCOUNT_NAME")
BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY", "PUT_YOUR_STORAGE_KEY")
BLOB_CONTAINER = os.getenv("BLOB_CONTAINER", "images")


# ---------------- MICROSOFT LOGIN (ENTRA ID) ----------------

AZURE_CLIENT_ID = "cd35ac97-1a68-4b4e-b93b-b270d30ef472"

AZURE_CLIENT_SECRET = "iXU8Q~YxadQVlUM8wNnA3Jq85HBbaVhjfNa6GaSo"

AZURE_TENANT_ID = "f958e84a-92b8-439f-a62d-4f45996b6d07"

AZURE_REDIRECT_URI = "https://udacitycms-hsggc0fbb9cpfayv.centralus-01.azurewebsites.net/auth"
