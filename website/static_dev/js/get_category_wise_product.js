
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
                  if ($('.items-row').length){
                    window.history.pushState('','','?c='+data.data[0].category+'')
                    // window.location.replace(new_url)

                  if (data.data.length)
                  {console.log(data.data[0].category)
                    $('#no_results').hide();
                   $('.items_container').hide().filter('[data-ctype="'+data.data[0].category+'"]').show()
                 }
                 else{
                   $('.items_container').hide();
                    $('#no_results').show();
                    $('#no_results').text('No Results..').css({'margin':'20px','text-align':'center','color':'red'})
                 }
}
else{
  console.log('No')

}

                })
}

}


})
