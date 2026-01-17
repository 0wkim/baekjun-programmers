// FizzBuzz 

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./28702.txt");
const INPUT = (FS.toString().trim().split("\n")).map(Number);

// 백준에서 사용하는 node.js 버전에는 findLastIndex가 없음 

const listLength = INPUT.length;
let numberIndex;

for (let a = listLength - 1; a >= 0; a--) {
    if (!Number.isNaN(INPUT[a])) {
        numberIndex = a;
        break;
    }
}

let i = 0;
if (INPUT[numberIndex] === INPUT[listLength - 1]) {
    i = INPUT[numberIndex] + 1;
}
else {
    i = INPUT[numberIndex] + (listLength - numberIndex);
}

if (i % 15 === 0) {
    console.log("FizzBuzz");
} else if (i % 3 === 0) {
    console.log("Fizz");
} else if (i % 5 === 0) {
    console.log("Buzz");
} else {
    console.log(i);
}
