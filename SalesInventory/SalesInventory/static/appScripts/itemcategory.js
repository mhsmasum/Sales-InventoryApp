$(document).ready(function () {
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

    var saveForm = function () {
        var form = $(this).parentsUntil().find('form');
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#table tbody").html(data.html_list);
                    $("#modal").modal("hide");
                    toastr.success("Your Data is Save", "Successfully", { closeButton: !0, progressBar: !0 });
                }
                else {
                    $("#modal .modal-content").html(data.html_form);
                }
            },
            error: function (error) {
                toastr.error("Your Data is Not Save", "Error", { closeButton: !0, progressBar: !0 });
            }
        });
        return false;
    };

    /* Binding */

    // Create 
    $("#btn-new").click(loadForm);
    $(document).off("click", "#btn-save").on("click", "#btn-save", saveForm);
    // Update 
    $("#table").on("click", ".btn-edit", loadForm);
    $(document).off("click", "#btn-update").on("click", "#btn-update", saveForm);

    // Delete
    $("#table").on("click", ".btn-delete", loadForm);
    $(document).off("click", "#btn-delete").on("click", "#btn-delete", saveForm);
});