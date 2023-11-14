const startingMinutes = 1;
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
            var rewardEl = document.createElement("div");
            rewardEl.innerHTML = `
                <div class="card mx-auto w-50 reward">
                    <div class="card-body">
                    <h5 class="card-title">Claim your sticker!</h5>
                    <p class="card-text">You've just earned a sticker to your PomoAlbum.</p>
                    <a href="#" class="btn btn-primary">Open pack</a>
                </div>
            `;
            mainSection.append(rewardEl);
        }
    }
}