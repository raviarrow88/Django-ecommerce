$(document).ready(function(){
items = document.getElementsByClassName('update-cart')
// console.log(user)
for(i=0;i < items.length;i++ ) {
  items[i].addEventListener('click',function(){
      var product_id = this.dataset.product
      var action = this.dataset.action

      if (user === 'AnonymousUser'){


        addCookieProduct(product_id,action)

      }
      else{

      update_or_create_cart(product_id,action)
      console.log(product_id,action)
    }
  })
}


function addCookieProduct(product_id,action){
  console.log(product_id)
  if (action == 'add'){
    if (cart[product_id] == undefined){
      cart[product_id] = {'quantity':1}
    }
    else{
      cart[product_id]['quantity'] +=1
    }
  }

if (action=='remove'){
  cart[product_id]['quantity']-=1

  if (cart[product_id]['quantity']<=0){
    delete cart[product_id]
  }

}
console.log(cart)

document.cookie = 'cart='+ JSON.stringify(cart) + ";domain=;path=/"
// location.reload()

}


async function update_or_create_cart(product_id,action) {
  // console.log(product_id,action)

  data ={"product_id":product_id,"action":action}

await  fetch('/update_cart/',{
    method:'POST',
    headers: {
    'Content-Type': 'application/json'},
    body: JSON.stringify(data),
  })
  .then((response) => {return response.json()}
    // console.log(response)
    )
  .then((data)=>{

        // $('#cart-total').html(data['cart_value'])
    location.reload()

    console.log(data)
  },

  )
// return false;

}


})
