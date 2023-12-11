#!/usr/bin/node

const dict = require('./101-data').dict;
const output = {};
for (const dat in dict) {
  if (!output[dict[dat]]) output[dict[dat]] = [];
  output[dict[dat]].push(dat);
}
console.log(output);
