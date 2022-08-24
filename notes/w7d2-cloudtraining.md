# Day 31 - Cloud trainind

## Objective

We want our package to work in the cloud.

- Allow team members to collaborate
- Train with a virtual GPU.

Today we will read information from Google Big Query.
Run the model in a virtual machine.
And store the model.

## Application parameters

Move to livecode

```py
import os
os.environ
```

We are saving the model in the train and evaluation function.

## Google Cloud storage

### Buckets

Containers for **blobs**. No tree structure.
Unique _kebab-case_ naming.

```sh
REGION=europe-west1
PROJECT=project-id
BUCKET=bucket-name

gsutil ls                               # list buckets

gsutil mb \
    -l $REGION \
    -p $PROJECT \
    gs://$BUCKET                        # create bucket
```

### Blobs

**Immutable** data storage.
Best for unstructured data.

**URI** `gs://bucket-name/blob/name`

```sh
gsutil ls gs://$BUCKET             # list blobs at the root of the bucket
gsutil ls -r gs://$BUCKET          # recursively list all blobs

gsutil cp *.csv gs://$BUCKET/      # copy all CSVs in the cwd to the bucket's root
gsutil cp gs://$BUCKET/*.csv .     # copy all CSVs at the bucket's root to the cwd
```

Download **blob**

```python
from google.cloud import storage

BUCKET_NAME = "my-bucket"

storage_filename = "data/raw/train_1k.csv"
local_filename = "train_1k.csv"

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob(storage_filename)
blob.download_to_filename(local_filename)
```

Upload **blob**

```python
storage_filename = "models/random_forest_model.joblib"
local_filename = "model.joblib"

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob(storage_filename)
blob.upload_from_filename(local_filename)
```

## Virtual Machine

```sh
INSTANCE=my-instance

gcloud compute instances list
# list virtual machine's status

gcloud compute instances start $INSTANCE
# start instance
gcloud compute instances stop $INSTANCE
# stop instance
```
