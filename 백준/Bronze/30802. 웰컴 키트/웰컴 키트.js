// 웰컴 키트

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./30802.txt");
const INPUT = FS.toString().split("\n");

const n = Number(INPUT[0]);
const sizeCountList = (INPUT[1].split(" ")).map(Number);
const t = INPUT[2].split(" ")[0];
const p = INPUT[2].split(" ")[1];

let shirtSet;
const shirtSetCount = sizeCountList.reduce((acc, cur) => {
    shirtSet = Math.ceil(cur / t);
    return acc + shirtSet;
}, 0);

console.log(shirtSetCount);

const penSet = Math.floor(n / p);
const pens = n % p;

console.log(`${penSet} ${pens}`);
