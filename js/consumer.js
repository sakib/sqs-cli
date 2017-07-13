const AWS = require('aws-sdk');
const Consumer = require('sqs-consumer');

AWS.config.update({
  region: process.env.AWS_DEFAULT_REGION,
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
})

const app = Consumer.create({
  queueUrl: process.env.CONSUME_QUEUE,
  handleMessage: (message, done) => {
    console.log('message is ' + message.Body);
    done();
  },
  sqs: new AWS.SQS()
});

app.on('error', (err) => {
  console.log(JSON.stringify(err.message));
});

app.start();
