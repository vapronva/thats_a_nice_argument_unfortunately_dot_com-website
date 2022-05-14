// Original code by gavra on https://codepen.io/gavra/pen/tEpzn; modified by vapronva for https://thats-a-nice-argument-unfortunately.com

fetch("https://api.thats-a-nice-argument-unfortunately.com/v1/ip")
    .then(res => res.json())
    .then(data => {
        originalTextArray = data.result.final_list;
        textArrayLength = originalTextArray[0].length;
    });

const eachCharachterDelay = 23;
var startPositionArray = 0; // skipcq: JS-0239
const maxLinesAtTime = 50;
var currentTextPosition = 0; // skipcq: JS-0239
var contentOfaLine = ""; // skipcq: JS-0239
const nextLineDelay = 230;
const startTimeDelay = 2200;

function typewriter() { // skipcq: JS-0128
    let destination = document.getElementById("typedtext");
    contentOfaLine = " ";
    currentRow = Math.max(0, startPositionArray - maxLinesAtTime);
    while (currentRow < startPositionArray) {
        contentOfaLine += `${originalTextArray[currentRow++]}<br/>`;
    }
    destination.innerHTML = `${contentOfaLine}${originalTextArray[startPositionArray].substring(0, currentTextPosition)}_`;
    if (currentTextPosition++ === textArrayLength) {
        currentTextPosition = 0;
        startPositionArray++;
        if (startPositionArray !== originalTextArray.length) {
            textArrayLength = originalTextArray[startPositionArray].length;
            setTimeout(typewriter, nextLineDelay);
        }
    } else {
        setTimeout(typewriter, eachCharachterDelay);
    }
}

setTimeout(typewriter, startTimeDelay);