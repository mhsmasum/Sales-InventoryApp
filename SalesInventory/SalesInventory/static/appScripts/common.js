$(document).ready(function () {
    if ($($('#table tbody tr')[0]).hasClass('tblRow')){ 
    datatableDeclare();
    }
    function datatableDeclare(){ 
        $('#table').DataTable().destroy();
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
                    debugger; 
                    $("#table tbody").html(data.html_list);
                    if ($($('#table tbody tr')[0]).hasClass('tblRow')){ 
                        datatableDeclare();
                        } 
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
});