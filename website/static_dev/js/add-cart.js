$(document).ready(function(){
items = document.getElementsByClassName('update-cart')

for(i=0;i < items.length;i++ ) {
  items[i].addEventListener('click',function(){
      var product_id = this.dataset.product
      var action = this.dataset.action


      update_or_create_cart(product_id,action)
      console.log(product_id,action)
  })
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
