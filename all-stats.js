fetch('soveliss-stats.json')
    .then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
    })

    .then(data => {
        function displayJson(data, containerId) {
            const container = document.getElementById("data-container");
            container.innerHTML = ''; // Clear previous content

            function buildHtml(obj, parentElement) {
                for (const key in obj) {
                    if (typeof obj[key] === 'object' && obj[key] !== null) {
                        const nestedDiv = document.createElement('div');
                        nestedDiv.innerHTML = `<strong>${key}:</strong>`;
                        parentElement.appendChild(nestedDiv);
                        buildHtml(obj[key], nestedDiv); // Recursively handle nested objects
                    } else {
                        const p = document.createElement('p');
                        p.innerHTML = `<strong>${key}:</strong> ${obj[key]}`;
                        parentElement.appendChild(p);
                    }
                }
            }
            buildHtml(data, container);
    }

    displayJson(data, 'json-display');
})  