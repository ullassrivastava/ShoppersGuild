total = 0;
score = 0;


function Dollar(){
        total=total+1;
        alert(total);
        document.getElementById('packA_tb').value = "Package A: ";
        document.getElementById('score').innerHTML = "Score: " + score;
    }


function Dollar2(){
        total=total+2;
        alert(total);
        document.getElementById('packB_tb').value = "Package B: ";
    }


function Dollar3(){
        total=total+3;
        alert(total);
        document.getElementById('packC_tb').value = "Package C: ";
    }


function GrandTotal(){
    alert(total);
}