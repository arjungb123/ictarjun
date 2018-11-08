function  read(){
    console.log("testing succces");
    var name=document.getElementById("getname").value;
    console.log(name);
    var rno=document.getElementById("getregister").value;
    console.log(rno);
    var adn=document.getElementById("getad").value;
    console.log(adn);
    var age=document.getElementById("getage").value;
    console.log(age);
    if(age>=18)
    {
        alert("  u r eligible");
        console.log(" u r eligible");

    }
    else{
        alert("not eligible");
        console.log("not eligible");
    }
}