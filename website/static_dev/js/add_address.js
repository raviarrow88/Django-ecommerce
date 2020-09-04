// $(document).ready(function(){
//
// $('#save_address').submit(function(event){
//   event.preventDefault()
//   console.log($(this).serialize())
//   $.ajax({
//     url:'/create_address_api/',
//     method:'POST',
//     data:$(this).serialize(),
//     success:function(response){
//       console.log(response)
//       $('#userDialog').modal('show')
//       $('#response_mssg').text(response['message'])
//
//     },
//     error:function(response){
//     // console.log(message)
//     // console.log(textStatus)
//     // console.log(responseJSON.Error)
//     console.log(response.responseText);
//     console.log(response.responseJSON['Error'])
//       $('#userDialog').modal('show')
//       $('#response_mssg').text("Error:"+response.responseJSON['Error']).css('color','red')
//     }
//
//   });
// })
//
// })
