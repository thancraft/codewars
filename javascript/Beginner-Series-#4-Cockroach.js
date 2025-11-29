// Mengkonversi kecepatan kecoa dari km/h ke cm/s
// s (km/h) -> meter (*1000) -> cm (*100) -> detik (/60/60)
function cockroachSpeed(s) {
  return Math.floor(s * 1000 * 100 / 60 / 60) // Bulatkan ke bawah
}