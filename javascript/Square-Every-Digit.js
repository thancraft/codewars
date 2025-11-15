function squareDigits(num){
  return Number(num.toString().split('').map((a) => String(parseInt(a) * parseInt(a))).join(''));
}