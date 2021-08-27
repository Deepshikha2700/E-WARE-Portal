const express=require("express");
const app=express();
const path = require('path');
const router = express.Router();
app.use(express.static(__dirname));

app.get("/",function(request,response){
    // response.sendFile(path.join(__dirname+'index.html'));
    // console.log(__dirname);
response.sendFile(__dirname+"/index.html");
});
// app.use('/', router);
// app.listen(process.env.port || 3000);
app.listen(3000,function(){
    console.log("server started at 3000");
});
