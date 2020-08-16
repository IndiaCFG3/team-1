//jshint express6
const express= require('express');

//require the body parser
const bodyParser= require('body-parser');
const app= express();

//body Parser works with express so
//urlencoded is used to tap into form data
app.use(bodyParser.urlencoded({extended:true}));



//when https req is sent to the root homepage, i.e.,
//when somebody opens the homepage
app.get("/",function(req,res) {


  // --dirname is a CONSTANT which always
  //has the current working directory's
  //name
  res.sendFile(__dirname+"/student-registration.html");
  
});

//when somebody submits the form data on the homepage

app.post("/",function(req,res) {
  //the numbers are parsed as strings,
  // the response is stored in response. body . num1 (
    //name attribute of the input )
    res.sendFile(__dirname+"/success.html")
      console.log(req.body);      
      var request = require('request');
var options = {
  'method': 'POST',
  'url': 'http://127.0.0.1:8000/users/',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(req.body),

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
  
});

//to listen to https request to homepage
app.listen(3000,function(req,res) {
console.log("Server started on port 3000");

});
