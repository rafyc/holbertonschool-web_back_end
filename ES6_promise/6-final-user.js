import signUpUser from './4-user-promise.js'
import uploadPhoto from './5-photo-reject.js'

function handleProfileSignup(firstName, lastName, fileName) {
  const p1 = signUpUser(firstName, lastName)
  const p2 = uploadPhoto(fileName)
  return Promise.allSettled([p1, p2]).then((values) => {
    values.map((v) => ({ status: v.status, value: v.status === 'fulfilled' ? v.value : `${v.reason.name}: ${v.reason.message}` }))
  });
}

export default handleProfileSignup
