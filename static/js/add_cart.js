function aggcart(){
    var selectValue = document.getElementById('qty-select').value;
    var buttonValue = document.getElementById('add-cart-button').value;
    console.log('cantidad seleccionada:', selectValue);
    console.log('id del producto:', buttonValue);
}

document.getElementById('add-cart-button').addEventListener('click', aggcart);