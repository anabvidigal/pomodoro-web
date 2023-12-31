var packModal = new bootstrap.Modal(document.getElementById('exampleModal'));
var openedPackContent = document.getElementById('openedPackContent');
var openPackButton = document.getElementById('openPackButton');

const canvas = document.getElementById('confettiContainer');
const jsConfetti = new JSConfetti({ canvas }); 

if (openPackButton) {
    openPackButton.addEventListener('click', () => {
        // Subtract unopened packs by 1
        showRandomCard();
    });
}

document.getElementById('closeAndRedirect').addEventListener('click', () => {
    window.location.href = '/album';
});

function showRandomCard() {
    fetch('/get_random_card', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(function (response) {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(function (data) {
        const card = data[0];
        // Populate inside of modal
        openedPackContent.innerHTML = `
        <div class="card mx-auto w-50 reward">
                    <div class="card-body">
                        <img class="card-img-top" src="${card.Image}" alt="">
                        <h5 class="card-title">${card.Title}</h5>
                        <p>${card.Description}</p>
                    </div>
                </div>
        `;
    })
    .catch(function (error) {
        console.error('There was a problem with the fetch operaion:', error);
    });

    packModal.show();

    jsConfetti.addConfetti({
        emojis: ['🍅', '🥫'],
     })
}