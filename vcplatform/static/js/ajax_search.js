$(function(){	
	// console.log(" --------- MADE IT TO AJAX_SEARCH.JS ----------")
	$('#search-bar').keyup(function(){
		console.log(" --------- MADE IT TO AJAX_SEARCH.JS ----------")
		$.ajax({
			type : "POST",
			url : "search/",
			data : {
				"search_t": $("#search-bar").val(),
				"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
				// '{{csrf_token}}'				
			},
			success: function(data){
				// This works and alerts our screen that success
				// alert("Successful");
				$('#body1').html(data)
			},			
			dataType: 'html'
		});
	});
});

// function search_success(data, textStatus, jqXHR){
// 	$('#search_result').html(data)
// }