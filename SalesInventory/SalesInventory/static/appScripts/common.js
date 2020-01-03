$(document).ready(function () {
    SetMenuActive();
    // if ($($('#table tbody tr')[0]).hasClass('tblRow')){ 
        // var interval = setInterval(function () {
        //     if ($($('#table tbody tr')[0]).hasClass('tblRow')) {
        //         datatableDeclare();
        //         clearInterval(interval);
        //     }
        // }, 1000);
        
    // }
    
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal").modal("show");
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
                $('.iCheck').iCheck({
                    checkboxClass: "icheckbox_flat-green",
                    radioClass: "iradio_flat-green"
                });
                $('.select2').select2();
            },
            error: function (error) {
                toastr.error("Something Wrong", "Error", { closeButton: !0, progressBar: !0 });
            }
        });
    };

    var saveForm = function (form) {
        //var form = $(this).parentsUntil().find('form');
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                     //$("#table tbody").empty();
                    // $('#table').DataTable().destroy();
                    $("#table tbody").html(data.html_list);
                    //datatableDeclare();
                    $("#modal").modal("hide");
                    toastr.success("Your Data is "+data.data_operation, "Successfully", { closeButton: !0, progressBar: !0 });
                }
                else {
                    $("#modal .modal-content").html(data.html_form);
                }
            },
            error: function (error) {
                toastr.error("Something Wrong", "Error", { closeButton: !0, progressBar: !0 });
            }
        });
        return false;
    };

    /* Binding */

    // Create 
    $("#btn-new").click(loadForm);
    $(document).off("click", "#btn-save").on("click", "#btn-save", function(){
        var form = $(this).parentsUntil().find('form');
        if($(form).parsley().validate()){
            saveForm(form);
            $('#table').DataTable().destroy();
            datatableDeclare();
        }
    });
    // Update 
    $("#table").on("click", ".btn-edit", loadForm);
    $(document).off("click", "#btn-update").on("click", "#btn-update", function(){
        var form = $(this).parentsUntil().find('form');
        if($(form).parsley().validate()){
            saveForm(form);
           
        }
    });

    // Delete
    $("#table").on("click", ".btn-delete", loadForm);
    $(document).off("click", "#btn-delete").on("click", "#btn-delete", function(){
        var form = $(this).parentsUntil().find('form');
            saveForm(form);
    });
    $('.menu-item').click(function () {
         var selectedMenu = $(this).text().trim();
         localStorage.setItem('activeMenu', selectedMenu);
    });
    
});

function SetMenuActive() {
    var selectedMenu = localStorage.getItem('activeMenu');
    $(".menu-item").parent().removeClass('active');
    $(".menu-item").each(function (index1, obj1) {
        if ($(obj1).text().trim() == selectedMenu) {
            $(obj1).parentsUntil('li .nav-item').addClass('open');
            $(obj1).parent().addClass('active');
            // $(obj1).closest('.nav-item-submenu').each(function (index2, obj2) {
            //     if ($(obj2).find('a:first').parent().hasClass('nav-item-open') === false) {
            //         $(obj2).find('a:first').click();
            //     }
            // });
        }
    });
}
function datatableDeclare(){        
      if ( ! $.fn.DataTable.isDataTable( '#table') ) {
        $('#table').DataTable({
            bAutoWidth: true,
            responsive: true,
            lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
            //order: [[ 1, "asc" ]],
            dom: 'Bflrtip',
            buttons: {
                dom: {
                    button: {
                        className: 'btn btn-outline-primary'
                    }
                },
                buttons: [
                    'copy', 'csv', 'excel', 'pdf', 'print'
                ]
            }
        });
        $('.dt-buttons').addClass('datatable_button');
        $('.dataTables_filter').addClass('datatable_filter');
        $('.dataTables_length').addClass('datatable_length');
      }
      $('#table').parent().parent().css({'max-height':'350px','overflow':'auto'});
    }