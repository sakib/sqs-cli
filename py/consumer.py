#!/usr/bin/python
import boto3, os, random, string

sqs = boto3.client('sqs')

while True:

    msg = sqs.receive_message(
        QueueUrl = os.environ.get('SQS_CONSUME_QUEUE'),
        AttributeNames = ['All'],
        MaxNumberOfMessages = 1,
        VisibilityTimeout = 20,
        WaitTimeSeconds = 20
    )

    # no messages detected, continue loop
    if not 'Messages' in msg: continue

    content = msg['Messages'][0]
    print str(content)

    sqs.delete_message(
        QueueUrl = os.environ.get('SQS_CONSUME_QUEUE'),
        ReceiptHandle = content['ReceiptHandle']
    )
