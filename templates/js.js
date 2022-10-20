function registrarPersona(){
    $.ajax({
        url : `http://localhost:5000/api/customers`, 
        method: "GET",
        dataType: "json",
        success:function(response) {

           console.log(response)
        },

        error: function(req, status, err) {

           console.log(req, status, err)
        },

    });

}