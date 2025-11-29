function narcissistic(value) {
    return ('' + value).split('').reduce((p, c) => p + Math.pow(c, ('' + value).length), 0) == value;
}

// function narcissistic(value) {
//   const _value = String(value).split('');

//   let _result = 0;

//   for (ch of _value) {
//     const num = parseInt(ch, 0)

//     _result += Math.pow(num, String(value).split('').length);
//   }

//   return _result === value;
// }