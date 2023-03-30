const echoForm = document.querySelector('#echo-form');
const findForm = document.querySelector('#find-form');

if (echoForm) {
    echoForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        const result = await fetch('/api/echo', {
            method: 'POST',
            body: formData,
        }).then(response => response.json());
        alert(result.success ? 'C-ECHO successful!' : 'C-ECHO failed!');
    });
}

if (findForm) {
    findForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        const result = await fetch('/api/find', {
            method: 'POST',
            body: formData,
        }).then(response => response.json());
        const resultTable = document.createElement('table');
        const headerRow = resultTable.insertRow();
        const studyDateHeader = headerRow.insertCell();
        studyDateHeader.innerText = 'Study Date';
        const patientNameHeader = headerRow.insertCell();
        patientNameHeader.innerText = 'Patient Name';
        for (const study of result) {
            const row = resultTable.insertRow();
            const studyDateCell = row.insertCell();
            studyDateCell.innerText = study['(0008,0020)'].Value[0];
            const patientNameCell = row.insertCell();
            patientNameCell.innerText = study['(0010,0010)'].Value[0];
        }
        const resultContainer = document.querySelector('#result-container');
        resultContainer.innerHTML = '';
        resultContainer.appendChild(resultTable);
    });
}
