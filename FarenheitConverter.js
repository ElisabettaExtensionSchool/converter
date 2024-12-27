// (Celsius * 9/5) + 32 = Farenheit)

function tempConv(Celsius) {
    var conv = (Celsius*9/5)+32;
    var message = Celsius.toString() + " degrees Celsius are " + conv.toString() + " degrees Farenheit.";
    return message;
}
console.log(tempConv(21.5));
console.log(tempConv(-7));
console.log(tempConv(11));
console.log(tempConv(0));