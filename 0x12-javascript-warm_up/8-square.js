#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

if (isNaN(num) || num === 0) {
  console.log('Missing size');
} else {
  for (let j = 0; j < num; j++) {
    console.log('X'.repeat(num));
  }
}
