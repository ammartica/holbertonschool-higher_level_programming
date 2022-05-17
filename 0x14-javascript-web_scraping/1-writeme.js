#!/usr/bin/node
// Script that writes a string to a given file

const filename = process.argv[2];
const content = process.argv[3];
const fs = require('fs');

fs.writeFile(filename, content, 'utf-8', err => {
  if (err) {
    console.err(err);
  }
});
