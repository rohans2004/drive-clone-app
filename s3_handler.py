import boto3
import os

s3 = boto3.client('s3')

bucket_name = ""

def set_bucket_name(name):
    global bucket_name
    bucket_name = name

def upload_to_s3(file, filename):
    s3.upload_fileobj(file, bucket_name, filename)
    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{filename}"
    return s3_url

def delete_from_s3(filename):
    s3.delete_object(Bucket=bucket_name, Key=filename)

