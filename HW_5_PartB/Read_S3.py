import boto3
import sys

# Set up the S3 client
s3 = boto3.client('s3')

# Specify the bucket name and object key of the HTML file
bucket_name = 'my-python-application-bucket'
object_key = 'index.html'

# Retrieve the HTML file contents from S3
try:
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    html = response['Body'].read().decode('utf-8')
except Exception as e:
    print('Error retrieving file from S3:', e)
    sys.exit(1)

# Print the HTML contents to the command window
print(html)
