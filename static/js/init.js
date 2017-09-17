(function($){
  $(function(){
    $('.carousel.carousel-slider').carousel({fullWidth: true});
    $('.button-collapse').sideNav();
    $('.modal').modal();
    Materialize.updateTextFields();
    $('select').material_select();
  }); // end of document ready
})(jQuery); // end of jQuery name space
