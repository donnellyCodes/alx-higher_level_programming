#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const [firstArg, secondArg] = process.argv.slice(2);
const firstInt = parseInt(firstArg, 10);
const secondInt = parseInt(secondArg, 10);
console.log(add(firstInt, secondInt));
