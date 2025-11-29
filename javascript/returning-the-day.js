// Mengembalikan nama hari berdasarkan nomor (1-7)
function whatday(num) {
    var nomor = num;
    var text;
    switch (nomor) {
        case 1:
            text = "Sunday";
            break;
        case 2:
            text = "Monday";
            break;
        case 3:
            text = "Tuesday";
            break;
        case 4:
            text = "Wednesday";
            break;
        case 5:
            text = "Thursday";
            break;
        case 6:
            text = "Friday";
            break;
        case 7:
            text = "Saturday";
            break;
        default: // Jika angka di luar 1-7
            text = 'Wrong, please enter a number between 1 and 7';
            break;

    }
    return text;

}



