import boto3

def lambda_handler(event, context):
    # Initialize the S3 client for the us-east-1 region
    s3 = boto3.client('s3', region_name='us-east-1')

    # List S3 buckets
    response = s3.list_buckets()

    # Extract bucket names
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]

    return {
        'statusCode': 200,
        'body': bucket_names
    }
