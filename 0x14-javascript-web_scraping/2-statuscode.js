#!/usr/bin/node
// Script that displays the status code of a GET request

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url).then(function (response) {
  console.log('code: ' + response.status);
}).catch(function (error) {
  console.log('code: ' + error.response.status);
});
