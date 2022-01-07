function checkPattern() {
    let values = document.getElementById('rgb').value;
    let rgbCodes = values.split(",");
    const userKeyRegExp = /^([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|25[0-5])$/;

    if (rgbCodes[0].match(userKeyRegExp) && rgbCodes[1].match(userKeyRegExp) && rgbCodes[2].match(userKeyRegExp)) {
        ConvertRGBtoHex(parseInt(rgbCodes[0]), parseInt(rgbCodes[1]), parseInt(rgbCodes[2]));
    }
    else {
        alert("Please enter in following format: x,y,z - where x y z represents rgb value from 0 up to 255");
    }
}

function ColorToHex(color) {
    let hexadecimal = color.toString(16);
    return hexadecimal.length == 1 ? "0" + hexadecimal : hexadecimal;
}

function ConvertRGBtoHex(red, green, blue) {
    document.getElementById("hexForm").innerHTML = "#" + ColorToHex(red) + ColorToHex(green) + ColorToHex(blue);
    return "#" + ColorToHex(red) + ColorToHex(green) + ColorToHex(blue);
}