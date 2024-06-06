// main.js
document.getElementById('percentageElement').addEventListener('click', async () => {
    try {
        const response = await fetch('http://localhost:3001/get'); // Fetch the number from the server
        const data = await response.json();
        const randomNumber = data.number;

        // Set the data-percent attribute in elementProgress.html
        const percentageElement = document.getElementById('percentageElement');
        percentageElement.setAttribute('data-percent', randomNumber);
    } catch (error) {
        console.error('Error fetching number:', error);
    }
});
