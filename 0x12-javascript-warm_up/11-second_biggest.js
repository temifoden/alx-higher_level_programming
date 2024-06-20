#!/usr/bin/node

// Extract arguments from the command line, ignoring the first two elements (which are 'node' and the script name)
const args = process.argv.slice(2);

// If no arguments are passed or only one argument is passed, print 0
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all arguments to integers and sort them in descending order
  const sortedIntegers = args.map(Number).sort((a, b) => b - a);
  
  // Find the second biggest integer
  const secondBiggest = sortedIntegers[1];
  
  console.log(secondBiggest);
}
