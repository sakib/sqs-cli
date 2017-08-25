# sqs-cli

These tools constitute a Python Command Line Interface to Amazon SQS.

See the README.md in the root directory of this repository for info on
semantics, links to further info on SQS, etc.

## Usage

Make sure to export the following environment variables.

- ```AWS_DEFAULT_REGION```
- ```AWS_ACCESS_KEY_ID```
- ```AWS_SECRET_ACCESS_KEY```
- ```SQS_CONSUME_QUEUE```
- ```SQS_PRODUCE_QUEUE```
- ```SQS_PURGE_QUEUE```

For Python peeps,

```
$ cd py
$ virtualenv venv
$ pip install -r pip.req
$ ./echo.py
$ ./purge.py
$ ./consumer.py
$ ./producer.py <msg1> <msg2> ...
```
