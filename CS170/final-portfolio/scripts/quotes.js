const quote = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Do one thing every day that scares you. - Eleanor Roosevelt",
    "The best way to predict the future is to create it. - Abraham Lincoln",
    "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "If you’re going through hell, keep going. - Winston Churchill",
    "Life isn’t about finding yourself. It’s about creating yourself. - George Bernard Shaw",
    "Don’t wait. The time will never be just right. - Napoleon Hill",
];

function getRandomquote() {
    const randomIndex = Math.floor(Math.random() * quote.length);
    return quote[randomIndex];
}

function printquote() {
    console.clear();
    console.log("Here’s a random piece of wisdom for you:");
    console.log(getRandomquote());
}

printquote();
