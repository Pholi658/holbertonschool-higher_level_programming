#!/usr/bin/node

const parameter1 = process.argv[2];
const parameter2 = process.argv[3];

if (parameter1 === undefined) {
    console.log('No argument');
}else {
    console.log(parameter1);
}
