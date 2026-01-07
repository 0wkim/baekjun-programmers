// A+B-C

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./31403.txt");
const numbers = (FS.toString().split("\n")).map(Number);

const numberSum = numbers[0]+numbers[1]-numbers[2];

console.log(numberSum);

const numbersToString = numbers.toString().split(",");

console.log(numbersToString[0] + numbersToString[1] - numbersToString[2]);