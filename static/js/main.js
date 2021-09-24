
$(document).ready(function(){
    $('#submits').click(function(event){
        event.preventDefault();
        $("fm").trigger("reset");
        location.reload();
        
    })
})
