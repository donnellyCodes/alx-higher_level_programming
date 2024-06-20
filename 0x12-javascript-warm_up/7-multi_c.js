#!/usr/bin/node
const [firstArg] = process.argv.slice(2);
const count = parseInt(firstArg, 10);
if (isNaN(count)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
