const inputField = document.querySelector(".input");

setInterval(() => {
  let hours = dayjs().format("HH");
  let minutes = dayjs().format("mm");
  let seconds = dayjs().format("ss");

  inputField.innerHTML = `${hours}<span class="colon">:</span>${minutes}:${seconds}`;
  console.log(`${hours}:${minutes}:${seconds}`);
}, 1000);
