/**
 * Created by gbis-954 on 2016/11/3.
 */
var i = 0;
for (i = 0; i <= 10; i++) {
    if (i == 3) {
        continue;
    }
    document.write("The number is " + i);
    document.write("<br/>");
}

window.onload = function(){

    var oUl = document.getElementById('ul1');
    alert(oUl.childNodes[0].nodeType);

    //alert(oUl.childNodes.length);
}


