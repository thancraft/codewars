// Kuadratkan setiap digit dari angka (contoh: 123 -> 149)
function squareDigits(num) {
  // Pisah tiap digit -> kuadratkan -> gabung lagi
  return Number(num.toString().split('').map((a) => String(parseInt(a) * parseInt(a))).join(''));
}