// Hapus setiap elemen dengan index ganjil, sisakan yang index genap
function removeEveryOther(arr) {
    return arr.filter((_, index) => index % 2 == 0) // Ambil hanya index 0, 2, 4, dst
}