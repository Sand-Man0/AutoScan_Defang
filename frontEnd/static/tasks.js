document.addEventListener('DOMContentLoaded', () => {

    fetch('/static/tasks.json')
        .then(response => response.json())
        .then(tasks => {
            createTaskTable(tasks);
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });

    function createTaskTable(tasks) {
        const tbody = document.querySelector('#taskTable tbody');

        tbody.innerHTML = '';

        tasks.forEach((task, index) => {
            const row = document.createElement('tr');


            const nameCell = document.createElement('td');
            nameCell.textContent = task.name;
            row.appendChild(nameCell);

           
            const statusCell = document.createElement('td');
            statusCell.textContent = task.status;
            row.appendChild(statusCell);

            
            const progressCell = document.createElement('td');
            const progress = document.createElement('progress');
            progress.value = task.progress;
            progress.max = 100;
            progress.textContent = `${task.progress}%`;
            progressCell.appendChild(progress);
            row.appendChild(progressCell);

            
            const dateCell = document.createElement('td');
            dateCell.textContent = task.date;
            row.appendChild(dateCell);

            const controlCell = document.createElement('td');

            const startButton = document.createElement('button');
            startButton.classList.add('btn');
            startButton.textContent = 'Start';

            const stopButton = document.createElement('button');
            stopButton.classList.add('btn');
            stopButton.textContent = 'Stop';

            const removeButton = document.createElement('button');
            removeButton.classList.add('btn');
            removeButton.textContent = 'Remove';

            const editButton = document.createElement('button');
            editButton.classList.add('btn');
            editButton.textContent = 'Edit';

           
            removeButton.addEventListener('click', () => {
                removeTask(index); 
            });

            controlCell.appendChild(startButton);
            controlCell.appendChild(stopButton);
            controlCell.appendChild(removeButton);
            controlCell.appendChild(editButton);

            row.appendChild(controlCell);

            tbody.appendChild(row);
        });
    }

    function removeTask(index) {
        fetch(`/remove_task/${index}`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            console.log('Task removed:', data);
       
            fetch('/static/tasks.json')
                .then(response => response.json())
                .then(tasks => {
                    createTaskTable(tasks); 
                });
        })
        .catch(error => {
            console.error('Error removing task:', error);
        });
    }
});

