from storages.backends.azure_storage import AzureStorage
from dotenv import load_dotenv
import os

load_dotenv()
BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY")

class AzureMediaStorage(AzureStorage):
    account_name = 'plank' # Must be replaced by your <storage_account_name>
    account_key = BLOB_STORAGE_KEY # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'plank' # Must be replaced by your storage_account_name
    account_key =   BLOB_STORAGE_KEY # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None