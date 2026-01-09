// 최대공약수와 최소공배수 

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./2609.txt");
const INPUT = (FS.toString().trim().split(" ")).map(Number);

let a = INPUT[0];
let b = INPUT[1];
let c;

while (c !== 0) {
    c = a % b;
    if (c === 0) break; 
    a = b;
    b = c;
}

const gcd = b;
const lcm = (INPUT[0]*INPUT[1])/gcd;

console.log(`${gcd}\n${lcm}`);