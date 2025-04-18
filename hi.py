import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()

# Print the names of the buckets
print("List of S3 Buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")

