<!doctype html>
<html>
<head>
<title>Quantum = cool</title>
<style>

.txtbox{
    border: 3px solid black;
    height: 370px;
    width: 750px;
    font-size: 60px;
    text-transform: lowercase;
}

.button{

background-color: #BB0000;
border: 1px solid black;
color: white;
padding: 5px 10px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 30px;
}


</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
<script>
$(document).ready(
    function(){
        $("#box").val("")
        
       $("#quantum").click(function(){
           $.get("/quantumstr.py?n=100",function(data){
               $("#box").val(data);
           });
       });


        $('#box').keypress(function (e) {
            v = $("#box").val();

            s = "";
            for(var i = 0;i<v.length;i++){
                    var c = v.charCodeAt(i)
                    if((65 <= c && c <= 90)|| (97 <= c && c <= 122)){
                            s += v[i];

                    }
            }
            
            $("#box").val(s);            
            if(e.keyCode == 8)
            {
                return true;
            }
            if($("#box").val().length >=100){
                    return false;
            }
            $("#box").val($("#box").val().toLowerCase())
            var txt = String.fromCharCode(e.which);
            if (!txt.match(/[a-zA-Z]/)) {
                    return false;
            }
        });
});


</script>
</head>

<body><center>
<form action="test.py" method="post">
<textarea id="box" class="txtbox" name="data" spellcheck="false"></textarea>
<br />

<input type="submit" value="Test" class="button" /> 
</form><br />
<button id="quantum" class="button">Quantum</button>
<span class="count"></span>
</center></body>
</html>
