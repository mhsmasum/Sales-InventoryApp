$(document).ready(function(){
    if($('#table tbody .tblRow').length>0){
        datatableDeclare();
    }
}); 
$(document).off("ifChecked", "#tbl tbody .tblRow .isbaseuom").on("ifChecked", "#tbl tbody .tblRow .isbaseuom", function(){
if($(this).is(':checked')){
    $('#tbl tbody .tblRow').find('.isbaseuom').not(this).iCheck('uncheck');
}
$('.iCheck').iCheck({
    checkboxClass: "icheckbox_flat-green",
    radioClass: "iradio_flat-green"
});
});


$(document).off("click", ".btn-row-add").on("click", ".btn-row-add", function(){
    var tblRow = $(this).closest('.tblRow');
    var isbaseuom = $(tblRow).find('.isbaseuom').is(':checked');
    $(tblRow).find('td:last').remove();
    $(tblRow).append('<td><input type="checkbox"  name="isbaseuom[]" class="isbaseuom iCheck"></td>');
    var $clone =  $(tblRow).clone().find('input').val('').end();
     $(tblRow).after($clone);
     $(tblRow).find('.isbaseuom').prop('checked', isbaseuom);
    $('.iCheck').iCheck({
        checkboxClass: "icheckbox_flat-green",
        radioClass: "iradio_flat-green"
    });
});

$(document).off("click", ".btn-row-remove").on("click", ".btn-row-remove", function(){
    var tblRow = $(this).closest('.tblRow');
    if($(tblRow).find('.uomid').val() === ""){
        var lastRow = $(tblRow).clone().find('input').val('').end();
        $(tblRow).remove();
        if($('#tbl tbody tr').length===0){
            $(lastRow).find('td:last').remove();
            $(lastRow).append('<td><input type="checkbox"  name="isbaseuom[]" class="isbaseuom iCheck"></td>');
            $('#tbl tbody').append(lastRow);
            $('.iCheck').iCheck({
                checkboxClass: "icheckbox_flat-green",
                radioClass: "iradio_flat-green"
            });
        }
    }else{
        var jsonData = {};
        jsonData["unitbasisname"] = $.trim($(".unitbasisname").val());
        jsonData["uom_name"] = $.trim($(".uom_name").val());
        jsonData["uom_shortname"] = $.trim($(".uom_shortname").val());
        jsonData["isactive"] = $('.isactive').is(':checked');
        
        var jsonObj = [];
        var detailObj = {};
        detailObj["uomid"] = $.trim($(tblRow).find('.uomid').val());
        detailObj["uomdetails_name"] = $.trim($(tblRow).find('.uomdetails_name').val());
        detailObj["uomdetails_shortname"] =  $.trim($(tblRow).find('.uomdetails_shortname').val());
        detailObj["convertionvalue"] =$.trim($(tblRow).find('.convertionvalue').val());
        detailObj["isbaseuom"] = $(tblRow).find('.isbaseuom').is(':checked');
        jsonObj.push(detailObj);
        jsonData["UomDetails"] = jsonObj;
        deleteUomDetails(tblRow,jsonData);
    }
    
    
});

$(document).off("click", "#btn-saveuom").on("click", "#btn-saveuom", function(){
    var form = $(this).parentsUntil().find('form');
    if($(form).parsley().validate()){
        var obj=saveobject();
        saveUomForm(form,obj);
        // $('#table').DataTable().destroy();
        // datatableDeclare();
    }
});
$(document).off("click", "#btn-updateuom").on("click", "#btn-updateuom", function(){
    var form = $(this).parentsUntil().find('form');
    if($(form).parsley().validate()){
        var obj=saveobject();
        saveUomForm(form,obj);
        // $('#table').DataTable().destroy();
        // datatableDeclare();
    }
});
function saveobject(){
    var jsonData = {};
       jsonData["unitbasisname"] = $.trim($(".unitbasisname").val());
       jsonData["uom_name"] = $.trim($(".uom_name").val());
       jsonData["uom_shortname"] = $.trim($(".uom_shortname").val());
       jsonData["isactive"] = $('.isactive').is(':checked');
       
       var jsonObj = [];
        $('#tbl tbody tr').each(function(index,tblRow) { 
            var detailObj = {};
            detailObj["uomid"] = $.trim($(tblRow).find('.uomid').val());
            detailObj["uomdetails_name"] = $.trim($(tblRow).find('.uomdetails_name').val());
            detailObj["uomdetails_shortname"] =  $.trim($(tblRow).find('.uomdetails_shortname').val());
            detailObj["convertionvalue"] =$.trim($(tblRow).find('.convertionvalue').val());
            detailObj["isbaseuom"] = $(tblRow).find('.isbaseuom').is(':checked');
            jsonObj.push(detailObj);
        });

        jsonData["UomDetails"] = jsonObj;
        return jsonData;
}

var saveUomForm = function (form,obj) {
    AjaxSetup();
    //var form = $(this).parentsUntil().find('form');
    $.ajax({
        //contentType: "application/json; charset=utf-8",
        data: JSON.stringify({'obj': obj}),
        url: form.attr("action"),
        // data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
            if (data.form_is_valid) {
                $("#table tbody").html(data.html_list);
                datatableDeclare();
                $("#modal").modal("hide");
                toastr.success("Your Data is "+data.data_operation, "Successfully", { closeButton: !0, progressBar: !0 });
            }
            else {
                $("#modal .modal-content").html(data.html_form);
            }
        },
        error: function (error) {
            toastr.error("Error StatusText : "+error.statusText + " And Status : "+error.status, "Error", { closeButton: !0, progressBar: !0 });
        }
    });
    return false;
};

var deleteUomDetails = function (tblRow,obj) {
    AjaxSetup();
    //var form = $(this).parentsUntil().find('form');
    $.ajax({
        //contentType: "application/json; charset=utf-8",
        data: JSON.stringify({'obj': obj}),
        url: 'deletedetails/',
        // data: form.serialize(),
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.form_is_valid) {
                var lastRow = $(tblRow).clone().find('input').val('').end();
                $(tblRow).remove();
                if($('#tbl tbody tr').length===0){
                    $(lastRow).find('td:last').remove();
                    $(lastRow).append('<td><input type="checkbox"  name="isbaseuom[]" class="isbaseuom iCheck"></td>');
                    $('#tbl tbody').append(lastRow);
                    $('.iCheck').iCheck({
                        checkboxClass: "icheckbox_flat-green",
                        radioClass: "iradio_flat-green"
                    });
                }    
            toastr.success("Your Data is "+data.data_operation, "Successfully", { closeButton: !0, progressBar: !0 });
            }
            else {
                $("#modal .modal-content").html(data.html_form);
            }
        },
        error: function (error) {
            toastr.error("Error StatusText : "+error.statusText + " And Status : "+error.status, "Error", { closeButton: !0, progressBar: !0 });
        }
    });
    return false;
};

function AjaxSetup(){
    $.ajaxSetup({ 
beforeSend: function(xhr, settings) {
   function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) == (name + '=')) {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }
   if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
       // Only send the token to relative URLs i.e. locally.
       xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
   }
} 
});
}