""" This script creates an S3 bucket and uploads a file to it. """
import boto3


BUCKET_NAME = "voca-game"
REGION = "us-west-2"
s3 = boto3.client("s3", region_name=REGION)

def create_s3_bucket():
    """ Create an S3 bucket in the specified region. """

    # Create S3 client

    # Create the bucket
    try:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print(
            f"Bucket '{BUCKET_NAME}' created successfully")
    except Exception as e:
        print(f"Failed to create bucket: {e}")


def upload_file_to_s3():
    """ Upload a file to an S3 bucket. """
    # Create S3 client
    #s3 = boto3.client("s3")

    # Upload the file
    try:
        s3.upload_file('vocabulary.json', BUCKET_NAME, 'vocabulary_json')
        print("File uploaded successfully")
    except Exception as e:
        print(f"Failed to upload file: {e}")

if __name__ == "__main__":
    create_s3_bucket()
    upload_file_to_s3()