document.getElementById('searchButton').addEventListener('click', function() {
    let username = document.getElementById('username').value;

    if (!username) {
        alert('Por favor, introduce un nombre de usuario.');
        return;
    }

    fetch(`/github-report/${username}`)
        .then(response => response.json())
        .then(data => {

            const reportDiv = document.getElementById('report');
            reportDiv.innerHTML = '';

            if (data.error) {
                reportDiv.innerHTML = `<p>${data.error}</p>`;
            } else {
                let reportContent = `
                    <p><strong>Nombre:</strong> ${data.name || 'No disponible'}</p>
                    <p><strong>Fecha de creación:</strong> ${data.created_at}</p>
                    <p><strong>Repositorios:</strong> ${data.public_repos}</p>
                    <h3>Repositorios:</h3>
                    <ul>
                `;

                data.repositories.forEach(repo => {
                    reportContent += `
                        <li>
                            <strong>${repo.name}</strong>
                            <br>Lenguaje más usado: ${repo.most_used_language || 'No disponible'}
                            <br>Lenguajes usados: ${repo.languages.join(', ')}
                        </li>
                    `;
                });

                reportContent += '</ul>';
                reportDiv.innerHTML = reportContent;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hubo un error al obtener los datos. Inténtalo de nuevo más tarde.');
        });
    });