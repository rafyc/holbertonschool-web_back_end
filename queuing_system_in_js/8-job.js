const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw Error(`Jobs is not an array`)
  }
  jobs.forEach(job => {
    const newJob = queue
      .create('push_notification_code_3')
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${newJob.id}`);
        }
      });
    newJob.on('failed', (errorMessage) => { console.log(`Notification ${newJob.id} failed: ${errorMessage}`); })
      .on('complete', () => { console.log(`Notification ${newJob.id} completed`); })
      .on('progress', (progress, data) => { console.log(`Notification job ${newJob.id} ${progress}% complete`); })
  });
}

export default createPushNotificationsJobs;
