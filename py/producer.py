#!/usr/bin/python
import boto3, os, random, string

sqs = boto3.client('sqs')

def gen_random_string(n=7):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

sqs.send_message(
    QueueUrl = os.environ.get('SQS_PRODUCE_QUEUE'),
    MessageGroupId = 'test-group',
    MessageDeduplicationId = gen_random_string(),
    MessageBody = sys.argv[1:]
)
