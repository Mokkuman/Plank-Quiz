from storages.backends.azure_storage import AzureStorage
BLOB_STORAGE_KEY = '3cIf3GRswWU31ct/sA/vpMexILDsE9CO+MfnimGAd3X/zZcjVFsUD76hQtTJEa0CfhXllzOjhnY6+ASt29/0nw=='

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