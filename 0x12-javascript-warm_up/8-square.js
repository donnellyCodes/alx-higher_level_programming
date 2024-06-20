#!/usr/bin/node
const [firstArg] = process.argv.slice(2);
const size = parseInt(firstArg, 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  const line = 'X' .repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}
