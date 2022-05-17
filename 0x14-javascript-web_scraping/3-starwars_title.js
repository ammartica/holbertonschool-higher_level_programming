#!/usr/bin/node
// Script that prints the title of a Star Wars movie where episode
// number matches a given integer

const axios = require('axios').default;
const num = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + num;

axios.get(endpoint).then(function (response) {
  console.log(response.data.title);
});
