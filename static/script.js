document.getElementById('searchButton').addEventListener('click', function() {
    let username = document.getElementById('username').value.trim();

    if (!username) {
        alert('Por favor, introduce un nombre de usuario.');
        return;
    }

    console.log(`Buscando usuario: ${username}`)

    fetch(`/github?user=${username}`)
    .then(response => response.json())
    .then(data => {
        console.log("Datos recibidos:", data);

        const reportDiv = document.getElementById('report');
        reportDiv.innerHTML = '';

        if (data.error) {
            reportDiv.innerHTML = `<p>${data.error}</p>`;
            return; 
        }

        if (!Array.isArray(data.repositories)) { 
            console.error("Error: 'repositories' no es un array.", data);
            reportDiv.innerHTML = `<p>Error en los datos recibidos.</p>`;
            return;
        }

        let reportContent = `
            <p><strong>Nombre:</strong> ${data.Nombre || 'No disponible'}</p>
            <p><strong>Fecha de creación:</strong> ${data["Fecha de creación"] || 'No disponible'}</p>
            <p><strong>Repositorios:</strong> ${data.Repositorios || 'No disponible'}</p>
            <h3>Repositorios:</h3>
            <ul>
        `;

        data.repositories.forEach(repo => {
            let languages = Array.isArray(repo.lenguajes) ? repo.lenguajes : [];
            let languagesList = languages.length > 0 ? languages.join(', ') : 'No disponible';

            reportContent += `
                <li>
                    <strong>${repo.nombre}</strong>
                    <br>Lenguaje más usado: ${languagesList.length > 0 ? languagesList[0] : 'No disponible'}
                    <br>Lenguajes usados: ${languagesList}
                </li>
            `;
        });

        reportContent += '</ul>';
        reportDiv.innerHTML = reportContent;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al obtener los datos. Inténtalo de nuevo más tarde.');
    });
});