#!/usr/bin/node
const [firstArg] = process.argv.slice(2);
const number = parseInt(firstArg, 10); // convert to integer
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
