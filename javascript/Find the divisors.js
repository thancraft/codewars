function divisors(integer) {
    let r = []
    for (let i = 2; i < integer; i++) {
        if (integer % i == 0) r.push(i)
    }
    let res = r.length !== 0 ? r : `${integer} is prime`
    return res
}