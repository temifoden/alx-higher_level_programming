#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], process.argv.slice(3).join(' '), 'utf8', function (error) {
  if (error){
    console.error(error);
    return;
  }
  console.log("File written successfully");
});
