// // // // // DARK MODE // // // // //

let darkMode = localStorage.getItem('darkMode');

const darkModeToggle = document.querySelector('#dark_mode_toggle');

const enableDarkMode = () => {

    // Add "dark mode" to body's class list
    document.body.classList.add('dark_mode');

    // Update the class of the toggle switches so their appearance changes
    darkModeToggle.classList.add("on");

    // Change the aria checks so the buttons change appearance
    darkModeToggle.setAttribute("aria-checked", "true");

    // Store the users preference in their local storage
    localStorage.setItem('darkMode', 'enabled')

};

const disableDarkMode = () => {

    // remove "" from the body's class list
    document.body.classList.remove('dark_mode');

    // Update the class of the toggle switches so their appearance changes
    darkModeToggle.classList.remove("on");

    // Change the aria checks so the buttons change appearance
    darkModeToggle.setAttribute("aria-checked", "false");

    // Store the users preference in their local storage
    localStorage.setItem('darkMode', null);

};

// When page loads (before the event listener runs) we need to check what is in the local storage

if (darkMode === "enabled") {

    enableDarkMode();

}

darkModeToggle.addEventListener('click', () => {

    // check the darkMode variable again upon click
    darkMode = localStorage.getItem('darkMode');

    // if the darkMode var is set to null then run enable function
    // if the darkMode var is set to "enabled" then run disable function
    if (darkMode !== "enabled") {
        enableDarkMode();  
    } else {
        disableDarkMode();
    };

});

// some JS for if we want to change the src of an element in the move to and from dark mode
        
    // if (document.body.classList.contains("dark-theme")) {
    //     ________.src = "";  
    // } else {
    //     ________.src = "";
    // }










// // // // // CUSTOM AUDIO PLAYER // // // // //










// // // // // CUSTOM VIDEO PLAYER // // // // //










// // // // // DYNAMIC LOGO ROTATION // // // // //

// I think this should help for mobiles. I want the logo to rotate based on the gyroscope. https://va3c.github.io/three.js/examples/misc_controls_deviceorientation.html

let constrain = 30; // Furthest reach. The larger the number, the more constrained the movement is.

let logo = document.getElementById("logo"); // Which element or elements is rotated

function transforms(x, y) {

    let calcX = -(y - (window.innerHeight / 2)) / constrain; // y coordinate - (viewport heigh / 2) / constraint variable

    let calcY = (x - (window.innerWidth / 2)) / constrain; //
  
    return "perspective(100px) "
        + "   rotateX("+ calcX +"deg) "
        + "   rotateY("+ calcY +"deg) ";

};

function transformElement(el, xyEl) {

    el.style.transform  = transforms.apply(null, xyEl);

};

document.onmousemove = function(e) {

    let xy = [e.clientX, e.clientY];
    let position = xy.concat([logo]);

    var x = e.clientX - (window.innerWidth / 2);
    var y = e.clientY - (window.innerHeight / 2);
    var coor = "X coords: " + x + ", Y coords: " + y;

    // // FOR TESTING - this will write the coordinates onto the webpage in a <p> element
    // document.getElementById("co-ords").innerHTML = coor;

    window.requestAnimationFrame ( function() { // animate the element's movement

        transformElement(logo, position); // Call the transform function with the element as argument 1 and the position of the mouse as argument 2

    } );

};





// if ( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
//     // some code..
// } else {

// };







// // // // // PARTICLES ANIMATION // // // // //

let canvas; // create a canvas variable
let context; // create a context variable that will fill in the canvas

let fpsInterval = 1000 / 30; // the denominator is frames-per-second
let now;
let then = Date.now();

let x = 250;
let y = 150;
let size = 10;
let xChange = randInt(-10, 10);
let yChange = randInt(-10, 10);


document.addEventListener("DOMContentLoaded", init, false); // command to have it happen after page is loaded

function init() {

    canvas = document.querySelector("canvas"); // ?????
    context = canvas.getContext("2d"); // the "context" that fills the above canvas

    draw();

}

function draw() {

    window.requestAnimationFrame(draw);

    let now = Date.now(); // all of this makes it run at 30fps
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);

    context.clearRect(0, 0, canvas.width, canvas.height); // clear the canvas entirely so that it doesn't leave a trail
    context.fillStyle = "yellow"; // tell context what style you want the fill to be
    context.fillRect(x, y, size, size); // tell context to create a filled rectangle at x 250, y 150 and make it 10 px wide, 10 px tall
    x = x + xChange;
    y = y + yChange;

    if (x < 0) {
        xChange = xChange * -1;
    } else if (x + size > canvas.width) {
        xChange = xChange * -1;
    }

    if (y < 0) {
        yChange = yChange * -1;
    } else if (y + size > canvas.height) {
        yChange = yChange * -1;
    }

}

function randInt(min, max) {

    return Math.round(Math.random() * (max - min)) + min;

}










// // // // // ROT13 CYPHER // // // // //

function rot13(str) {

    var solved = "";
    
    for (var i=0; i<str.length; i++) {
    
        var asciiNum = str[i].charCodeAt();
        if (asciiNum >= 65 && asciiNum <=77) {
            solved += String.fromCharCode(asciiNum + 13);
        } else if (asciiNum >=78 && asciiNum <=90) {
            solved += String.fromCharCode(asciiNum - 13);
        } else {
            solved += str[i];
        }
    }
    
    return solved;

};
  
// [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
  
rot13("VS LBH PNA ERNQ GUVF, LBHE EBG13 PBQR VF JBEXVAT!")