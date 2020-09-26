$(document).ready(function(){
  if (user == 'AnonymousUser'){
    $('#loginModal').modal({
      backdrop: 'static',
        keyboard: false
    });

  }
  else {}

  $("#save_address").click(function(event){
if (user == 'AnonymousUser'){
  event.preventDefault()
}
})


  $('#placeOrderBtn').click(function(){
      if(user == 'AnonymousUser'){
        setTimeout(function(){

                $('#loginModal').modal({
                  backdrop: 'static',
                    keyboard: false
                })

        },1000);
      }else{
        fetch('/config/')
        .then((result)=> {return result.json();})
        .then((data) => {
          console.log("key",data)
          const stripe = Stripe(data.publicKey);

          fetch('/create_checkout_session/')
          .then((result)=>  {return result.json()})
          .then((data)=>{
            console.log(data)
            return stripe.redirectToCheckout({sessionId: data.sessionId})
          })
          .then((res)=>{
            console.log(res)
          });

        });



      } //else

  }) //click




});
