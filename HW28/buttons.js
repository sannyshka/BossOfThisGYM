// Task2

const addFriendBtn = document.getElementById('addFriendBtn');
const friendCountElement = document.getElementById('friendCount');
let friendCount = Math.floor(Math.random() * 100);
    friendCountElement.textContent = `Кількість друзів: ${friendCount}`;


addFriendBtn.addEventListener('click', () => {
        friendCount++;
        friendCountElement.textContent = `Кількість друзів: ${friendCount}`;
    });




// Task3

const addFriendBtn = document.getElementById('addFriendBtn');
const friendCountElement = document.getElementById('friendCount');

let friendCount = Math.floor(Math.random() * 100);
    friendCountElement.textContent = `Кількість друзів: ${friendCount}`;

addFriendBtn.addEventListener('click', () => {
        addFriendBtn.textContent = "Очікується підтвердження";
        addFriendBtn.disabled = true;

        friendCount++;
        friendCountElement.textContent = `Кількість друзів: ${friendCount}`;
    });


// Task4

const sendMessageBtn = document.getElementById('sendMessageBtn');

    const defaultColor = 'btn-outline-info';
    const changedColor = 'btn-outline-warning';

    let isColorChanged = false;

    function changeButtonColor() {
        if (isColorChanged) {
            sendMessageBtn.classList.remove(changedColor);
            sendMessageBtn.classList.add(defaultColor);
        } else {
            sendMessageBtn.classList.remove(defaultColor);
            sendMessageBtn.classList.add(changedColor);
        }
        isColorChanged = !isColorChanged;
    }

    sendMessageBtn.addEventListener('click', () => {
        changeButtonColor();
    });

// Task5

 const addFriendBtn = document.getElementById('addFriendBtn');
    const jobOfferBtn = document.getElementById('jobOfferBtn');

    jobOfferBtn.addEventListener('click', () => {
        addFriendBtn.style.display = 'none';
    });

    jobOfferBtn.addEventListener('dblclick', () => {
        addFriendBtn.style.display = 'block';
    });



// Task6

const addHomeworkBtn = document.getElementById('addHomeworkBtn');
    const homeworkTableBody = document.getElementById('homeworkTableBody');

    addHomeworkBtn.addEventListener('click', () => {

        const newRow = document.createElement('tr');
        const homeworkName = document.createElement('td');
        const grade = document.createElement('td');
        homeworkName.textContent = 'Круте завдання';
        grade.textContent = '10/10';
        newRow.appendChild(homeworkName);
        newRow.appendChild(grade);

        homeworkTableBody.appendChild(newRow);
    });