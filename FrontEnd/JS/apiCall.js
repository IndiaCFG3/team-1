$(document).ready(function(){
  $("#submitbtn").click(function(){
console.log("Hi")
var settings = {
  "url": "http://127.0.0.1:8000/users/",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify([{"id":id,"name":name,
  "role":"Teacher","username":username,
  "email":email,"password":pwd,
  "organisation":org,"courseID":cid,
  "courseName":cname}]),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
  });
});