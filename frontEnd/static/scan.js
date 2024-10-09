document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (e) {
        e.preventDefault(); 

        const taskName = document.getElementById('task-name').value;
        const scanConfig = document.getElementById('scan-config').value;
        const targetHost = document.getElementById('target-host').value;
        const startImmediately = document.querySelector('input[name="schedule"]:checked').value === "immediately";
        const scheduleDate = document.getElementById('schedule-date').value;
        const scheduleTime = document.getElementById('schedule-time').value;
        const emailReport = document.getElementById('email-report').value;

        const taskData = {
            name: taskName,
            scanConfig: scanConfig,
            targetHost: targetHost,
            date: startImmediately ? new Date().toISOString().split('T')[0] : scheduleDate,
            time: startImmediately ? new Date().toISOString().split('T')[1].slice(0, 5) : scheduleTime,
            emailReport: emailReport
        };

   
        fetch('/add_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(taskData),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Group added successfully!');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
