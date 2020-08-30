
$(document).ready(function(){


k = document.querySelectorAll('.drop_ele')

//alert(k[0].innerHTML)

for (i=0;i<k.length;i++){

k[i].addEventListener('click',function(event){

selected_category=$(this).text()


var url = '/category/?category='+selected_category.trim()

var req = new Request(url)
sendRequest(req,event)
})


function sendRequest(req,event){
   // var url = window.location.href;
   console.log(req)
  fetch(req,{
    method:'GET',
    headers:{
      'Content-Type':'application/json'
    }
  }).then((response) => {
        return response.json()
            }).then((data)=>{
                  var new_url = req['url']

                  console.log(data)
                  if (window.location.pathname=='/'){


                  content = data.fh
                  $('.container').html(content)
                  // encoded_url = encodeURIComponent()
                  window.history.pushState('','','?category='+data.type+'')


                }

                else{
                  console.log(new_url)

                  location.replace(location.origin+'/?category='+data.type+'')
                }
                })
}

}


})
