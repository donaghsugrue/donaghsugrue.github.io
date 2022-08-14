let canvas;
let context;

let fpsInterval = 1000 / 30; // the denominator is frames-per-second
let now;
let then = Date.now();

let threshold = 50;
let points = [];

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    draw();
}

function draw() {
    window.requestAnimationFrame(draw);
    
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);

    let q = {
        x : randint(0, 500),
        y : randint(0, 500)
    }

    for (let p = 1; p <= points.length; p += 1) {
        if ((dist(p,q)) < threshold)  {
        // //             draw a line between q and p
        }
    }

    //After the loop in draw(), push q onto the array called points.
    points.push(q);
}

function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}

// function dist(p,q) {
//     sqrt( (p.x - q.x)2 + (p.y - q.y)2 )
// }

// You will need to look up the JavaScript for drawing lines

// The functions/variables that you will use are:
//     strokeStyle
//     beginPath
//     moveTo
//     lineTo
//     stroke

// Optional: The whole thing will look much prettier if you vary the line width to make it inversely proportional to the distance.