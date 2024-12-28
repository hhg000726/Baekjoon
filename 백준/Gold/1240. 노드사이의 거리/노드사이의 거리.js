let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const fl = input[0].split(' ');
const N = Number(fl[0]);
const M = Number(fl[1]);
const dists = [];
const cups = [];
let answer = 0

class Node {
  constructor(value) {
    this.value = value;
    this.neighbors = [];
  }
}

const Nodes = [null];

for (let i = 0; i < N; i++) {
  Nodes.push(new Node(`Node ${i + 1}`));
}

for (let i = 0; i < N - 1; i++) {
  dists[i] = input[i + 1].split(' ').map(x => parseInt(x));
}

for (let i = 0; i < M; i++) {
  cups[i] = input[i + N].split(' ').map(x => parseInt(x));
}

for (let i = 0; i < N - 1; i++) {
  Nodes[dists[i][0]].neighbors.push([dists[i][1], dists[i][2]]);
  Nodes[dists[i][1]].neighbors.push([dists[i][0], dists[i][2]]);
}

for (let i = 0; i < M; i++) {
  q = [[cups[i][0], 0]];
  visited = Array(N + 1).fill(false);
  visited[cups[i][0]] = true;
  while (q) {
    const t = q.shift();
    if (t[0] == cups[i][1]) {
      answer = t[1];
      break;
    }
    else {
      Nodes[t[0]].neighbors.forEach(element => {
        if (!visited[element[0]]) {
          visited[element[0]] = true;
          q.push([element[0], element[1] + t[1]]);
        }
      });
    }
  }
  console.log(answer);
}