(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('select').material_select();
    $('select').on('change', function() {
        var str = this.value;
        var pos = str.lastIndexOf(':');
        var length = str.length;
        var encryptions = str.slice(pos+1,length);

        if(encryptions=="False")
        {
            document.getElementById("password").removeAttribute("required");
            $('#passDiv').css('display', "none");
        }
        else
        {
            document.getElementById("password").required = true;
            $('#passDiv').css('display',"block");
        }

    })
  }); // end of document ready



})(jQuery); // end of jQuery name space