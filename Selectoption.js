    function show() { 
        if(document.getElementById('option1').style.display=='none') { 
            document.getElementById('option2').style.display='none';
            document.getElementById('option1').style.display='block'; 
            
        } 
     
        
        return false;
    } 
    
    
    
       function show2() { 
        if(document.getElementById('option2').style.display=='none') { 
            document.getElementById('option1').style.display='none';
            document.getElementById('option2').style.display='block'; 
        } 
   
        return false;
    } 