const displayMessage = (str) => {
  process.stderr.write(str);
};

module.exports = displayMessage;
