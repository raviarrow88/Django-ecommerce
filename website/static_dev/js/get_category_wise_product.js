
$(document).ready(function(){


k = document.querySelectorAll('.drop_ele')

//alert(k[0].innerHTML)

for (i=0;i<k.length;i++){

k[i].addEventListener('click',function(){

selected_category=$(this).text()


var url = '/category/?type='+selected_category.trim()

var req = new Request(url)
sendRequest(req)
})


function sendRequest(req){
   var url = window.location.href;
   console.log(req)
  fetch(req,{
    method:'GET',
    headers:{
      'Content-Type':'application/json'
    }
  }).then((response) => {
        return response.json()
            }).then((data)=>{
                  d = JSON.stringify(data)
                  

                  new_url = req['url']
                  window.history.pushState('','', new_url)
                })
}

}


})
