function filter_list(l) {
    return l.filter((v) => typeof v == 'number');
}

// function filter_list(l) {
//   // Kembalikan array baru dengan elemen yang bukan string
//   return l.filter((item) => Number.isInteger(item));
// }