// Hashing

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./15829.txt");
const INPUT = FS.toString().split("\n");

const length = Number(INPUT[0]);
const alphabetString = INPUT[1];

const r = 31;
const m = 1234567891;
const alphabetList = Array.from({length: 26}, (_, i) => String.fromCharCode(97+i));

let hashSum = 0;
let power = 1;
for (let i = 0; i < length; i++) {
    let a = alphabetList.indexOf(alphabetString[i]) + 1;
    hashSum = (hashSum + a * power) % m;
    power = (power * r) % m;
}

console.log(hashSum);