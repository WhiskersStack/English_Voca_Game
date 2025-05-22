""" Download a file from S3 bucket using Boto3. """
import boto3

BUCKET_NAME = "voca-game"
S3_KEY = "vocabulary_json"
DOWNLOAD_PATH = "vocabulary2.json"


def download_file_from_s3():
    """ Download a file from an S3 bucket. """

    # Create S3 client
    s3 = boto3.client("s3")

    # Download file
    try:
        s3.download_file(BUCKET_NAME, S3_KEY, DOWNLOAD_PATH)
        print("File downloaded successfully")
    except Exception as e:
        print(f"❌ Download failed: {e}")


if __name__ == "__main__":
    download_file_from_s3()
