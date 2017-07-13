#!/usr/bin/python
import boto3, os, random, string

sqs = boto3.client('sqs')

def gen_random_string(n=7):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

while True:

    try:
        msg = sqs.receive_message(
            QueueUrl = os.environ.get('AWS_CONSUME_QUEUE'),
            AttributeNames = ['All'],
            MaxNumberOfMessages = 1,
            VisibilityTimeout = 20,
            WaitTimeSeconds = 20
        )
    except Exception as e:
        print "Failed to receive message!", str(e)
        continue

    # no messages detected, continue loop
    if not 'Messages' in msg: continue

    content = msg['Messages'][0]

    sqs.delete_message(
        QueueUrl = os.environ.get('AWS_CONSUME_QUEUE'),
        ReceiptHandle = content['ReceiptHandle']
    )

    sqs.send_message(
        QueueUrl = os.environ.get('AWS_PRODUCE_QUEUE'),
        MessageGroupId = 'test-group',
        MessageDeduplicationId = gen_random_string(),
        MessageBody = content['Body']
    )

