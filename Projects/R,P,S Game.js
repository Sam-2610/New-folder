const choices = ['rock', 'paper', 'scissors'];

function playGame(playerChoice) {
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];
    console.log("Player Choice:", playerChoice);
    console.log("Computer Choice:", computerChoice);

    if (playerChoice === computerChoice) {
        console.log("It's a tie!");
    } else if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        console.log("You win!");
    } else {
        console.log("You lose!");
    }
}
