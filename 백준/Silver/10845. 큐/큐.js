// 큐

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./10845.txt");
const INPUT = FS.toString().trim().split("\n");

let queue = [];
let head = 0;

function pushIn(number, arr) {
    arr.push(number);
}

function popIn(arr) {
    if (arr.length - head === 0) {
        console.log(-1);
    } else {
        console.log(arr[head]);
        head++; // 배열은 건드리지 않고 인덱스만 수정 (head가 배열의 시작)
    }
}

function size(arr) {
    console.log(arr.length - head);
}

function isEmpty(arr) {
    if (arr.length - head === 0) {
        console.log(1);
    } else if (arr.length - head !== 0) {
        console.log(0);
    }
}

function front(arr) {
    if (arr.length - head === 0) {
        console.log(-1);
    } else {
        console.log(arr[head]);
    }
}

function back(arr) {
    if (arr.length - head === 0) {
        console.log(-1);
    } else {
        console.log(arr.at(-1));
    }
}

INPUT.forEach(cmd => {
    if (cmd.includes("push")) {
        let number = Number(cmd.slice(5));
        pushIn(number, queue);
    } else if (cmd.includes("pop")) {
        popIn(queue);
    } else if (cmd.includes("size")) {
        size(queue);
    } else if (cmd.includes("empty")) {
        isEmpty(queue);
    } else if (cmd.includes("front")) {
        front(queue);
    } else if (cmd.includes("back")) {
        back(queue);
    }
});
