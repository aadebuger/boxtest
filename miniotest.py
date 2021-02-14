from minio import Minio
#from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
#                         BucketAlreadyExists)

# Initialize minioClient with an endpoint and access/secret keys.
from minio.error import InvalidResponseError
minioClient = Minio('localhost:9000',
                    access_key='MINIO_ROOT_USER',
                    secret_key='MINIO_ROOT_PASSWORD',
                    secure=False)


try:
    minioClient.make_bucket("boxhr")
except InvalidResponseError as err:
    print(err)
# Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
#try:
#       minioClient.fput_object('androidimg', '20200119140300012.png', '2060S.png')
#except InvalidResponseError as err:
#       print(err)