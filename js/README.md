# sqs-cli

### JavaScript Command Line Interface to Amazon Simple Queue Service

Make sure to export the following environment variables.

- ```AWS_DEFAULT_REGION```
- ```AWS_ACCESS_KEY_ID```
- ```AWS_SECRET_ACCESS_KEY```
- ```SQS_CONSUME_QUEUE```
- ```SQS_PRODUCE_QUEUE```
- ```SQS_PURGE_QUEUE```

For JavaScript peeps,

```
$ npm i
$ node purge.js
$ node consumer.js
$ node producer.js <msg1> <msg2> ...
```
