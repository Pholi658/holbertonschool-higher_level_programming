#!/usr/bin/node

const parameter1 = process.argv[2];

if (parameter1 === undefined) {
  console.log('No argument');
} else {
  console.log(parameter1);
}
