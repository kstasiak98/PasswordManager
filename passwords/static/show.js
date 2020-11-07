const csrf = $('input[name="csrfmiddlewaretoken"]').val();

$('.show_password').on('click', function(){

    $.ajax({
        url: '/list/',
        type: 'post',
        data: {
            password_id: $(this).attr('id'),
            csrfmiddlewaretoken: csrf
        },
        cache : false,
        success: function(response){
            $(".modal-body").text("Your password is: " + response.password);
            $("#myModal").modal('show');
            },
        });
    });

    $('#myModal').on('hidden.bs.modal', function () {
        $('.modal-body').html('');
    });