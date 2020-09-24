$(document).ready(function(){
  if (user == 'AnonymousUser'){
    $('#loginModal').modal({
      backdrop: 'static',
        keyboard: false
    });

  }
  else {}

  $("#save_address,#placeOrderBtn").click(function(event){
if (user == 'AnonymousUser'){
  event.preventDefault()

    setTimeout(function(){

            $('#loginModal').modal({
              backdrop: 'static',
                keyboard: false
            })

    },1000);
}

  })
});
