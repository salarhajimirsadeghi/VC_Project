$(function(){	
	console.log(" --------- MADE IT TO AJAX_SEARCH.JS ----------")
	$('#search-bar').keyup(function(){
		console.log(" --------- MADE IT TO AJAX_SEARCH.JS ----------")
		$.ajax({
			type : "POST",
			url : "search/",
			data : {
				'search_text': $("#search-bar").val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
				// '{{csrf_token}}'				
			},
			success: search_success,
			dataType: 'html'
		});
	});
});

function search_success(data, textStatus, jqXHR){
	$('#search_result').html(data)
}