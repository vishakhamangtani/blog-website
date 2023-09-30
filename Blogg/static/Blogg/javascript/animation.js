const contentArray =["The pen is your paintbrush, and the words are your strokes. Create a masterpiece on the canvas of life.",
"In the library of life, let your words be the most compelling stories, inspiring countless chapters.",
"With each word you write, you plant a seed of wisdom that may one day grow into a forest of inspiration.",
"Words are the wings of the soul, and with them, you can soar to limitless heights of creativity and influence.",
"Embrace the power of your voice, for it has the potential to light the way in the darkest of times.",
"Your thoughts are the architects of your destiny, and your words are the builders of your dreams.",
"Let your words be the lighthouse, guiding lost ships to the shores of understanding and empathy.",
"Every word you write is a brushstroke on the canvas of your legacy. Paint it with purpose and passion.",
"In the symphony of life, your words can be the melody that moves hearts and ignites souls.",
"Write with the intent to inspire, for your words may be the spark that ignites the fire of greatness in others."]

const contentDiv = document.getElementById('quote');

let currentIndex = 0;

function changeContent() {
  contentDiv.style.opacity = 0;
  setTimeout(function () {
    contentDiv.textContent = contentArray[currentIndex];
    contentDiv.style.opacity = 1;
    currentIndex = (currentIndex + 1) % contentArray.length;
  }, 500); // 500 milliseconds for the fade effect
}

// Call the function initially and set an interval for every 5 seconds
changeContent();
setInterval(changeContent, 10000); // 5000 milliseconds (5 seconds)
