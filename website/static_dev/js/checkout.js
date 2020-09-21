$(document).ready(function(){
  if (user == 'AnonymousUser'){
    $('#loginModal').modal({
      backdrop: 'static',
        keyboard: false
    });

  }
  else {}

  $("#save_address,#placeOrderBtn").click(function(event){
    event.preventDefault()

    setTimeout(function(){

          if (user == 'AnonymousUser'){
            $('#loginModal').modal({
              backdrop: 'static',
                keyboard: false
            })
          }
    },1000);


  })
});
