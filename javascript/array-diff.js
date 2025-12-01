function arrayDiff(a, b) {
    return a.filter(val => !b.includes(val));
}