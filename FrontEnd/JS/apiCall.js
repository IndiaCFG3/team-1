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
            "data": JSON.stringify([{"id":1,"name":"Utkasrh",
            "role":"Student","username":"utkarsh114",
            "email":"utkarsh1148@gmail.co","password":"123hi;",
            "organisation":"Thapar Institute","courseID":"ahlh123234",
            "courseName":"App Development"}]),
          };
          
          $.ajax(settings).done(function (response) {
            console.log(response);
          });
    });
  });


