// Menghitung luas permukaan dan volume balok
function getSize(width, height, depth) {
    // Return [luas permukaan, volume]
    return [2 * (width * height + width * depth + height * depth), width * height * depth];
}