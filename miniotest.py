from minio import Minio
#from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
#                         BucketAlreadyExists)

# Initialize minioClient with an endpoint and access/secret keys.
from minio.error import InvalidResponseError
minioClient = Minio('localhost:9000',
                    access_key='minioadmin',
                    secret_key='minioadmin',
                    secure=False)


#try:
#    minioClient.make_bucket("boxhr")
#except InvalidResponseError as err:
#    print(err)
# Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
#try:
#       minioClient.fput_object('androidimg', '20200119140300012.png', '2060S.png')
#except InvalidResponseError as err:
#       print(err)
import json
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["s3:GetBucketLocation", "s3:ListBucket"],
            "Resource": "arn:aws:s3:::boxhr",
        },
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::boxhr/*",
        },
    ],
}
try:
    minioClient.set_bucket_policy("boxhr", json.dumps(policy)); 
except  Exception as e : 
    print("Error occurred: " + e); 