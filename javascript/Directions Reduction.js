function dirReduc(arr) {
    // function to check for the presence of invalid directions
    function hasInvalidDirections(array) {
        count = 0;
        for (let i = 0; i < array.length - 1; i++) {
            if (
                (array[i] === "NORTH" && array[i + 1] === "SOUTH") ||
                (array[i] === "SOUTH" && array[i + 1] === "NORTH") ||
                (array[i] === "EAST" && array[i + 1] === "WEST") ||
                (array[i] === "WEST" && array[i + 1] === "EAST")
            ) {
                count++;
            }
        }
        return count > 0;
    }

    // while loop to restart the the nested for-loop
    while (hasInvalidDirections(arr)) {
        for (let i = 0; i < arr.length; i++) {
            if (
                (arr[i] === "NORTH" && arr[i + 1] === "SOUTH") ||
                (arr[i] === "SOUTH" && arr[i + 1] === "NORTH") ||
                (arr[i] === "EAST" && arr[i + 1] === "WEST") ||
                (arr[i] === "WEST" && arr[i + 1] === "EAST")
            ) {
                arr.splice(i, 2);
            }
        }
    }

    return arr;
}