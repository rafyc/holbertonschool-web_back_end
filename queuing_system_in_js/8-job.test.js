import createPushNotificationsJobs from './8-job';
import { expect } from 'chai';
import kue from 'kue';

const queueName = 'push_notification_code_3';
const jobs = [
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  }];


const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit()
  });

  it('it check the number of jobs', () => {
    queue.createJob(queueName, jobs).save();
    expect(queue.testMode.jobs.length).to.equal(1);
  });

  it('should take the right queue', () => {
    queue.createJob(queueName, jobs).save();
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  })

  it('should take the right datas', () => {
    queue.createJob(queueName, jobs).save();
    expect(queue.testMode.jobs[0].data).to.eql([{
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account',
    }]);
  })

  it('should complete the progess', () => {
    queue.createJob(queueName, jobs).save();
    const job = queue.testMode.jobs[0];
    job.on('progress', () => {
      expect(job.progress).to.equal('active');
    });
    job.on('complete', () => {
      expect(job.progress).to.equal('complete');
    })
  })

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(44, queue)).throws(
      Error, 'Jobs is not an array',
    );
  });

  it('should throw an error if jobs is not an array', () => {
    expect(createPushNotificationsJobs([], queue)).equals(undefined);
  });

})
