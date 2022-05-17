#!/usr/bin/node
// Script that prints the number of movies where the character
// "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];

request({ url: url, json: true }, (error, response) => {
  if (error) {
    console.log('code: ', error);
  } else {
    const content = response.body.results;
    let count = 0;
    for (let i = 0; i < content.length; i++) {
      for (let j = 0; j < content[i].characters.length; i++) {
        if (content[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
