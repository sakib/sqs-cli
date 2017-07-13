const AWS = require('aws-sdk');
const Producer = require('sqs-producer');


var counter = 0;

AWS.config.update({
  region: process.env.AWS_DEFAULT_REGION,
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
});


const producer = Producer.create({
  queueUrl: process.env.PRODUCE_QUEUE,
  region: process.AWS_DEFAULT_REGION,
  sqs: new AWS.SQS()
});


producer.send([{
  id: 'id' + counter,
  groupId: 'test group yo',
  body: String(process.argv.splice(2)),
  deduplicationId: Math.random().toString(36).substring(7)
}], function(err) {
  counter += 1;
  if (err) console.log(err);
});


producer.queueSize(function (err, size) {
  if (err) console.log(err);
  console.log('there are ', size, ' messages on the queue');
});
