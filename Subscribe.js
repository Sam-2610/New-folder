function Subscribe(){
    const documentElement = document.querySelector('.hello');
    if(documentElement.innerText === 'Subscribe'){
        documentElement.innerHTML = 'Subscribed';
        documentElement.classList.add('is');
    } else {
        documentElement.innerHTML = 'Subscribe';
        documentElement.classList.remove('is');
    }
}