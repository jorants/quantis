$(document).ready(
	 function(){
		 // make sure the field is empty when back is pressed
		 if($(".error").length < 1){
			 $("#text").val("")
		 }

		 $("#quantum").click(function(){
			 $.get("/rand/100",function(data){
				 $("#text").val(data);
			 });
		 });

		 //make sure no more then 100 chars are entered and everything is lower case
		 $('#text').keypress(function (e) {
			 v = $("#text").val();

			 s = "";
			 for(var i = 0;i<v.length;i++){
				 var c = v.charCodeAt(i)
				 if(((65 <= c && c <= 90)|| (97 <= c && c <= 122)) && s.length <= 100 ){
					 s += v[i];
				 }
			 }

			 $("#text").val(s);

			 if(e.keyCode == 8)
				 {
					 return true;
				 }
			 if($("#text").val().length >=100){
				 $("#text").val($("#text").val().substring(0,100))
				 return false;
			 }
			 $("#text").val($("#text").val().toLowerCase())
			 var txt = String.fromCharCode(e.which);
			 if (!txt.match(/[a-zA-Z]/)) {
				 return false;
			 }
		 });
	 });
