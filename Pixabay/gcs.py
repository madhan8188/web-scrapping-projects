from google.cloud import storage
from google.oauth2 import service_account
projectname = 'profound-keel-253502'
bucketname = "quilt_plumbing_staging_data"
keypath = "/home/quilt/etl-plumbing/plumbing-key.json"

credentials = service_account.Credentials.from_service_account_file(keypath)
storage_client = storage.Client(credentials = credentials, project = projectname)
bucket = storage_client.get_bucket(bucketname)
blob = bucket.blob('Google_entities_etl31.csv')
blob.upload_from_filename('Google_entities_etl31.csv')
