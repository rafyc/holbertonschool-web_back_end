import { createPushNotificationsJobs } from './8-job';

import kue from 'kue';

const queue = kue.createQueue();

before(function () {
  queue.testMode.enter(true);
});

afterEach(function () {
  queue.testMode.clear();
});

after(function () {
  queue.testMode.exit()
});

it('does something cool', function () {
  queue.createJob('myJob', { foo: 'bar' }).save();
  queue.createJob('anotherJob', { baz: 'bip' }).save();
  expect(queue.testMode.jobs.length).to.equal(2);
  expect(queue.testMode.jobs[0].type).to.equal('myJob');
  expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
});
