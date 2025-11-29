function moveZeros(arr) {
    return arr.filter(function (x) { return x !== 0 }).concat(arr.filter(function (x) { return x === 0; }));
}

// function moveZeros(arr) {
//   const n = arr.length;
//     const temp = new Array(n);

//     // to keep track of the index in temp[]
//     let j = 0;

//     // Copy non-zero elements to temp[]
//     for (let i = 0; i < n; i++) {
//         if (arr[i] !== 0) {
//             temp[j++] = arr[i];
//         }
//     }

//     // Fill remaining positions in temp[] with zeros
//     while (j < n)
//         temp[j++] = 0;

//     // Copy all the elements from temp[] to arr[]
//     for (let i = 0; i < n; i++)
//         arr[i] = temp[i];
//   return arr
// }
