function Calculate(){
    const documentElement = document.querySelector('.hello');
    let cost = Number(documentElement.value);
    if(cost < 40){
        cost = cost + 10;
    }

    document.querySelector('.input').innerHTML = `$${cost}`;
   

}