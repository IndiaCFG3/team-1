$(document).ready(function(){
    $("#submitbtn").click(function(){
	console.log("Hi")
        var settings = {
            "url": "http://localhost:8000/users/",
            "method": "POST",
            "timeout": 0,
            "headers": {
              "Content-Type": "application/json",
            },
            "data": JSON.stringify([{
                "name":username,
                "password":pwd,
                "work":"login"
            }]),
          };
          
          

          $.ajax(settings).done(function (response) {
            console.log(response);
            if(response)
            {
                var redirectWindow = window.open('studentmain.html', '_blank');
                redirectWindow.location;
            }
            else
            {
                alert("Wrong Credentials");
            }
          });
    });
  });