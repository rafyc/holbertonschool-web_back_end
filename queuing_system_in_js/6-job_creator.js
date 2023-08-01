import kue from 'kue';

const queue = kue.createQueue();

const obj = {
  phoneNumber: '04040404',
  message: 'This is my phone',
}

const job = queue
  .create('push_notification_code', obj)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  })
job.on('failed', () => { console.log('Notification job failed'); })
job.on('complete', () => { console.log('Notification job completed'); })

