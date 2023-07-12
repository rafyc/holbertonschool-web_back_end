function getFullResponseFromAPI(success) {
  new Promise((success) => {
    if (success)
      return {
        status: 200,
        body: 'succes'
      }
  })
}
