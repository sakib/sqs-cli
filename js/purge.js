const AWS = require('aws-sdk');

AWS.config.update({
  region: process.env.AWS_DEFAULT_REGION,
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
})

const params = {
  QueueUrl: process.env.PURGE_QUEUE,
};

const sqs = new AWS.SQS();

sqs.purgeQueue(params, function(err, data) {
  if (err)  console.log(err, err.stack);  //error
  else      console.log(data);            //success
});

