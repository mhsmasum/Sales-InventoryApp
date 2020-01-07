$(document).ready(function(){
    if($('#table tbody .tblRow').length>0){
        datatableDeclare();
    }
});

$(document).off("change", ".description").on("change", ".description", function(){
   var itemDescription = [];
   $('.description').each(function(index,obj){
       if( $(obj).val() !==''){
        if($(obj).is('input')){
             itemDescription.push($(obj).val()); 
        }else if($(obj).is('select')){
            itemDescription.push($(obj).find(' option:selected').text());
        }
       }       
   });
   $('.ItemDescription').val(itemDescription.join(" - "));
});