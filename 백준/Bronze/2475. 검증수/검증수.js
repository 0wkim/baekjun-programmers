// 검증수

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./2475.txt");
const numbers = (FS.toString().split(" ")).map(Number);

const square_sum = numbers.reduce((acc, cur) => {
    return acc + cur**2;
}, 0);

const checksum = square_sum % 10;

console.log(checksum);