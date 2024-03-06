import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

const data = [
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
];

queue.testMode.enter();

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe('createPushNotificationsJobs', () => {
  it('should create two new jobs to the queue', () => {
    createPushNotificationsJobs(data, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(data[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(data[1]);
  });

  it('should throw error if the data is not an array', () => {
    expect(() => createPushNotificationsJobs('data', queue)).to.throw();
  });

  it('should throw error if the queue is not a kue queue', () => {
    expect(() => createPushNotificationsJobs(88675, 'queue')).to.throw();
  });

  it('should throw error if the data is not an array of objects', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw();
  });
});
