const startingMinutes = 0.1;
let time = startingMinutes * 60;
let countdownInterval;
let pause = true;
let reward = false;

const startButton = document.getElementById('start');
const pauseButton = document.getElementById('pause');
const countdownEl = document.getElementById('countdown');
const mainSection = document.getElementById('main');

startButton.addEventListener('click', () => {
    if (startButton.innerHTML == "Start") {
        pause = false;
        startButton.innerHTML = "Reset";
        countdownInterval = setInterval(updateCountdown, 1000);
    }
    else {
        pause = true;
        clearInterval(countdownInterval);
        time = startingMinutes * 60;
        updateCountdown();
        countdownEl.innerHTML = `${startingMinutes}:00`;
        startButton.innerHTML = "Start";
    }
});

pauseButton.addEventListener('click', () => {
    if (pauseButton.innerHTML == "Pause") {
        pause = true;
        pauseButton.innerHTML = "Resume"
    }
    else {
        pause = false;
        pauseButton.innerHTML = "Pause"
    }
    
});

function updateCountdown() {
    if (!pause) {
        const minutes = Math.floor(time / 60);
        let seconds = time % 60;

        seconds = seconds < 10 ? '0' + seconds : seconds;

        countdownEl.innerHTML = `${minutes}:${seconds}`;
        time--;

        if (time < 0) {
            clearInterval(countdownInterval);
            countdownEl.innerHTML = "00:00";
            reward = true;
        }

        if (reward == true) {
            showCard();
            givePack();
        }
    }
}

function showCard() {
    var rewardEl = document.createElement("div");
            rewardEl.innerHTML = `
            <form action="/album" method="post">
                <div class="card mx-auto w-50 reward">
                    <div class="card-body">
                    <h5 class="card-title">Claim your sticker!</h5>
                    <p class="card-text">You've just earned a sticker to your PomoAlbum.</p>
                    <button type="submit" id="claim" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-sm">Open pack</button>
                </div>
            </form>
            `;
            mainSection.append(rewardEl);

            const claimButton = document.getElementById('claim');

            claimButton.addEventListener('click', () => {
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
                    // Create a new modal element
                    rewardEl.innerHTML = `
                        <div class="card mx-auto w-50 reward">
                            <div class="card-body">
                            <img class="card-img-top" src="${data.image_url}" alt="">
                            <h5 class="card-title">${data.name}</h5>
                            <button type="button" id="claim" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-sm">See in the album</button>
                        </div>
                    `;
                })
                .catch(function (error) {
                    console.error('There was a problem with the fetch operaion:', error);
                });
            });
}

function givePack() {
    // Send data to the server increasing the amount of unopened packs by 1
    fetch('/give_pack', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(function (response) {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        console.log("Granted pack.")
    })
    .catch(function (error) {
        console.error('There was a problem with the fetch operaion:', error);
    });
}