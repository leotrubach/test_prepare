function busy_form() {
    $('form.answer').find('input, textarea').attr('disabled', 'disabled');
}

function data_sent(data) {
	if (data.success) {
	    if (data.correct) {
	        $('#a' + data.given_id)
	        	.removeClass('btn-primary')
	        	.addClass('btn-success');
	    } else {
	        $('#a' + data.given_id)
	        	.removeClass('btn-primary')
	        	.addClass('btn-danger');
	        $('#a' + data.correct_id)
	        	.removeClass('btn-primary')
	        	.addClass('btn-success');
	    }
    }
}

$(function(){
	$('form.answer').ajaxForm({
		success: data_sent,
        beforeSubmit: busy_form,
        dataType: 'json'});
});