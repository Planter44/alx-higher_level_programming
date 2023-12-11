#!/usr/bin/node
const fs = require('fs');
let ssd = '';
ssd = ssd.concat(fs.readFileSync(process.argv[2]));
ssd = ssd.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], ssd);
