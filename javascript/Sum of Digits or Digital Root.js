function digitalRoot(n) {
    let sums = n.toString().split('').reduce((acc, num) => acc + parseInt(num), 0);
    if (sums.toString().length >= 2) {
        sums = digitalRoot(sums);
    }
    return sums;
}