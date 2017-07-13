#!/usr/bin/python
import boto3, os

sqs = boto3.client('sqs')

sqs.purge_queue(
    QueueUrl = os.environ.get('SQS_PURGE_QUEUE')
)
