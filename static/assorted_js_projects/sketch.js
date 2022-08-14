// # c5c5c5 as a background, black text
// Use the commodore font

// https://youtu.be/55iwMYv8tGI

const density = "Ñ@#W$9876543210?!abc;:+=-,._";

let video;
// let asciiDiv;
let canvas;


// Frames per second, so that we don't overload anything
let fpsInterval = 1000 / 30; // the denominator is frames-per-second
let now;
let then = Date.now();


document.addEventListener("DOMContentLoaded", init, false);

function setup() {
  // noCanvas();
  
  video = createCapture(VIDEO);
  video.size(100, 48);
  
  // asciiDiv = createDiv(); // Rather than createDiv(), could we getElementById and put it in a Canvas?
  // canvas = document.querySelector("canvas");
}

function draw() {
  // video.loadPixels();
  let asciiImage = "";
  for (let j = 0; j < video.height; j++) {
    for (let i = 0; i < video.width; i++) {
      const pixelIndex = (i + j * video.width) * 4; // times 4 as there's 4 values. R, G, B and Alpha (transparency)
      const r = video.pixels[pixelIndex + 0];
      const g = video.pixels[pixelIndex + 1];
      const b = video.pixels[pixelIndex + 2];
      const avg = (r + g + b) / 3;
      const len = density.length;
      const charIndex = floor(map(avg, 0, 255, len, 0));

      const c = density.charAt(charIndex);
      if (c == " ") asciiImage += "&nbsp";
      else asciiImage += c;
    }
    asciiImage += "<br/>"
  }
  asciiDiv.html(asciiImage);
}





// const f = context.frame

// const {x, y} = coord


// Average of RGB 0 - 255 is a good measure of brightness. So like:
// brightness = (100 + 200 + 255) / 3 // RGB(100, 200, 255)
// steps = density.length() / 255 // based on how many ascii values we have

// noStroke();
// fill(avg);
// square(i * w, j * h, w);

// textSize(W);
// textAlign(CENTER, CENTER);
// text(, i * w + w * 0.5, j * h + h * 0.5);



// width = 500
// height = 500
// size = width / 10

// j x ( size x width ) + i x size + k % size + k / size x width





// //( 0   8   2   10
// //  12  4   14  6
// //  3   11  1   9
// //  15  7   13  5 )


// threshold = [
//   0,   48,  12,  60,  3,   51,  15,  63,
//   32,  16,  44,  28,  35,  19,  47,  31,
//   8,   56,  4,   52,  11,  59,  7,   55,
//   40,  24,  36,  20,  43,  27,  39,  23,
//   2,   50,  14,  62,  1,   49,  13,  61,
//   34,  18,  46,  30,  33,  17,  45,  29,
//   10,  58,  6,   54,  9,   57,  5,   53,
//   42,  26,  38,  22,  41,  25,  37,  21
// ]