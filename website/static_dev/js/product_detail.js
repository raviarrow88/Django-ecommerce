$(document).ready(function(){
  const leftBtn = $('#slideLeft');
  const rightBtn = $('#slideRight')

  let thumbs = $('.thumbnail')
  let activeImages = $('.active')
thumbs.each(e => thumbs.eq(e).mouseover(function(){
      if (activeImages.length > 0){
        // console.log(activeImages[0].li.removeClass('active'))
        // activeImages[0].removeClass('active')

        activeImages[0].classList.remove('active')
      }

      this.classList.add('active')

      $('.prod-d-img').attr('src',this.src)

})
);



  leftBtn.click(function(){
  $('#slider').animate({
     scrollLeft: "-=180px"
  },"slow");
});

  rightBtn.click(function(){
  $('#slider').animate({
     scrollLeft: "+=180px"
  },"slow");
});



});
