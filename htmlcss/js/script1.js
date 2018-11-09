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
    var p=x+y;
     alert(p);
  }

  if(oper=="-"){

    var q=x-y;
    alert(q);
  }
  if(oper=="*"){

  var r=x*y;
  alert(r);

      
  }if(oper=="%")
  {
      var s=x/y;
      alert(s);
  }










}