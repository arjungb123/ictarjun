function get()
{
    var a=document.getElementById("op1").value;
    var b=document.getElementById("op2").value;
    var x=parseInt(a);
    var y=parseInt(b);
    
    var c=document.getElementById("oper");
    var oper=(c.options[c.selectedIndex]).value;
    if(oper=="+")
    {
    var c=x+y;
     
  }

  if(oper=="-"){

    var c=x-y;
    
  }
  if(oper=="*"){

  var c=x*y;
  

      
  }if(oper=="%")
  {
      var c=x/y;
      
  }

document.getElementById("result").innerHTML="<table border=3><tr><td>"+c+"</td>,</tr><table>"








}