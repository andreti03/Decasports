var updateBtns = document.getElementsByClassName('create-bill')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click',function(){
        var cartID = this.dataset.cart
        var action = this.dataset.action
        console.log('cartID', cartID,'action', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            createBill(cartID, action)
        }
        
    })
    
}

function createBill(cartID, action){
    console.log('User is logged in, sending data...')

    if (action=='create') {
        var url ='/Create_bill/'
    }else{
        var url ='/factura/'
    }
    console.log('url:', url)
    console.log('cartID', cartID,'action', action)

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'cartID': cartID,'action': action}),
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data)
    })
}

