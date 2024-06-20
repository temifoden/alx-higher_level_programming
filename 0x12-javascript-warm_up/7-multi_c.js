#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(arr[0]);
  }
}
