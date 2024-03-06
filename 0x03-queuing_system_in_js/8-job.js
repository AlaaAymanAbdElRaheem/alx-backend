const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');
  jobs.forEach((jobData) => {
    const job = queue
      .create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
      });
  });

  queue.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  queue.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  queue.on('progress', (progress, data) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
};

module.exports = createPushNotificationsJobs;
