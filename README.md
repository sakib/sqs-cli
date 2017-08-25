# sqs-cli

This is a command line interface to Amazon Simple Queue Service.

## What Do?

This repository contains tools built in both JS and Python to perform actions
on AWS SQS distributed queues. They work on both standard and FIFO queues.

- `purge` removes all messages from a queue. Useful for when queues are acting
  up, for example, if reads/writes to a development queue are unresponsive.
- `consume` starts a daemon that continuously extracts messages from a queue
  and prints out the contents of the message that it contains.
- `produce` pushes a string from command line args to a queue.

You might test these out by creating a queue Q, starting a consumer to read
from Q in one terminal, producing a few messages onto Q in another terminal,
and purging Q from time to time.

## Setup

You're going to want at least one queue to mess around with. You can follow
[this link](https://aws.amazon.com/sqs/) and read "Get Started" and "FAQ".

The CLI requires that you export the following environment variables:

- ```AWS_DEFAULT_REGION``` - amazon aws credentials: region name
- ```AWS_ACCESS_KEY_ID``` - amazon aws credentials: access key
- ```AWS_SECRET_ACCESS_KEY``` - amazon aws credentials: secret key
- ```SQS_CONSUME_QUEUE``` - the URL of the queue that `consumer.js` will read messages from
- ```SQS_PRODUCE_QUEUE``` - the URL of the queue that `producer.js` will send messages to
- ```SQS_PURGE_QUEUE``` - the URL of the queue that `purge.js` will purge.

For JavaScript peeps,

```
$ cd js
$ npm i
$ node purge.js
$ node consumer.js
$ node producer.js <msg1> <msg2> ...
```

For Python peeps,

```
$ cd py
$ virtualenv venv
$ pip install -r pip.req
$ source venv/bin/activate
$ ./echo.py
$ ./purge.py
$ ./consumer.py
$ ./producer.py <msg1> <msg2> ...
```
