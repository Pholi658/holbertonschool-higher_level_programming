#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

if (process.argv.length <= 2){
    console.log('No arguments found')
}else {
    console.log('Arguments found')
}
