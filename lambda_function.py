import os
import sys

sys.path.insert(0, '/opt')
os.environ["PYTHONPATH"] = "/opt"
import lambda_initialize
import boto3


def lambda_handler(event, context):
    try:
        lambda_initialize.loadTests()
        lambda_initialize.loadBrowser(["headless-chromium", "chromedriver"])

        print("Starting test")
        os.system("python /var/task/test.py")
        print(os.system('find /tmp/results* -name "*" -type f'))
        upload_results_to_S3('/tmp/results', 'elearnio-automation', 'results')
    except Exception as e:
        exeMsg = type(e).__name__ + " : " + str(e)
        print(e)
        print(exeMsg)
        raise e


def upload_results_to_S3(output_directory, bucketname, folder_name):
    s3 = boto3.client('s3')
    files = os.listdir(output_directory)
    try:
        for i in files:
            source_filepath = output_directory + '/' + i
            destination_filepath = folder_name + '/' + i

            s3.upload_file(source_filepath, bucketname, destination_filepath)
    except Exception as e:
        print(e)

