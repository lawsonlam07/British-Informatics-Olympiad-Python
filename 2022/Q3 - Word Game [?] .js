const prompt = require("prompt-sync")();
let alpha = Array.from("/ABCDEFGHIJKLMNOPQRSTUVWXYZ");
let wordList = [];
let word = prompt("Enter a word: ").toUpperCase();
let finished = false


let score = 0
for (let v of word) {
   score += alpha.indexOf(v);
}


function findWords(target, arr, n = 1) {
   if (target === 0) {
       if (arr.join("") === word) {
           finished = true
           console.log(wordList.length + 1)
       }
       wordList.push(arr.join(""))
   }


   for (let i = 1; i < Math.min(target, 26) + 1; i++) {
       while (arr.length > n) {
           arr.pop();
       }


       if (arr[arr.length-1] !== alpha[i] && target - i >= 0) {
           arr.push(alpha[i]);
           if (!finished) {
               findWords(target - i, arr, n + 1);
           }
       }
   }
}


for (let i = 1; i < Math.min(score, 26) + 1; i++) {
   if (!finished) {
       findWords(score - i, [alpha[i]]);
   }
}
