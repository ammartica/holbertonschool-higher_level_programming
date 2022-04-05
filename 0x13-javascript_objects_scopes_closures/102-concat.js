#!/usr/bin/node
// Concats 2 files

const fs = require('fs');
let info = '';

info = info.concat(fs.readFileSync(process.argv[2]));
info = info.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], info);
