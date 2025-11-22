document.getElementById('detect-btn').addEventListener('click', async () => {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "Detecting food...";

    try {
        const response = await fetch('/detect', { method: 'POST' });
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `<p style="color:red">${data.error}</p>`;
        } else {
            let html = `<h2>Detected Food: ${data.food}</h2>`;
            html += "<h3>Nutrition Info:</h3><ul>";
            for (let key in data.nutrition) {
                html += `<li>${key}: ${data.nutrition[key]}</li>`;
            }
            html += "</ul>";
            resultDiv.innerHTML = html;
        }
    } catch (err) {
        resultDiv.innerHTML = `<p style="color:red">Error detecting food</p>`;
        console.error(err);
    }
});
