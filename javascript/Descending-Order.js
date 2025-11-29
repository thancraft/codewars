// Mengurutkan digit angka dari besar ke kecil
function descendingOrder(n) {
    // Ubah ke string -> pisah jadi array -> urutkan descending -> gabung lagi -> jadikan angka
    return Number(n.toString().split('').sort((a, b) => b - a).join(''))
}
