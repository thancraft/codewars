function spinWords(words) {
    return words.split(' ').map((word) => { return (word.length > 4) ? word.split('').reverse().join('') : word; }).join(' ');
}

// function spinWords(string){
//   return string.split(" ").map((word) => {
//   if(word.length >= 5){
//     return word.split("").reverse().join("");
//   }else{
//     return word
//   }

// }).join(" ");
// }
