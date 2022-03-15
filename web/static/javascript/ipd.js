// Original code by gavra on https://codepen.io/gavra/pen/tEpzn; modified by vapronva for https://thats-a-nice-argument-unfortunately.com
var originalTextArray;
var textArrayLength;

fetch("https://api.thats-a-nice-argument-unfortunately.com/v1/ip")
    .then(res => res.json())
    .then(data => {
        originalTextArray = data.result.final_list;
        textArrayLength = originalTextArray[0].length;
    });

var eachCharachterDelay = 23;
// var eachCharachterDelay = 0;
var startPositionArray = 0;
var maxLinesAtTime = 50;
var currentTextPosition = 0;
var contentOfaLine = '';
var nextLineDelay = 230;
var startTimeDelay = 2200;
// var nextLineDelay = 0;
// var startTimeDelay = 0;
var currentRow;

function typewriter() {
    contentOfaLine = " ";
    currentRow = Math.max(0, startPositionArray - maxLinesAtTime);
    var destination = document.getElementById("typedtext");
    while (currentRow < startPositionArray) {
        contentOfaLine += originalTextArray[currentRow++] + "<br/>";
    }
    destination.innerHTML = contentOfaLine + originalTextArray[startPositionArray].substring(0, currentTextPosition) + "_";
    if (currentTextPosition++ == textArrayLength) {
        currentTextPosition = 0;
        startPositionArray++;
        if (startPositionArray != originalTextArray.length) {
            textArrayLength = originalTextArray[startPositionArray].length;
            setTimeout("typewriter()", nextLineDelay);
        }
    } else {
        setTimeout("typewriter()", eachCharachterDelay);
    }
}

setTimeout("typewriter()", startTimeDelay);