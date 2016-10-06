$(document).ready(function() {
	const ids = [link1 = {
			button:'#editLinkOne',
			div:'#link1'
		},
		link2 = {
			button:'#editLinkTwo',
			div: '#link2'
		},
		link3 = {
			button:"#editLinkThree",
			div: '#link3'
		},
		link4 = {
			button:"#editLinkFour",
			div: "#link4"
		},
		link5 = {
			button: "#editLinkFive",
			div: "#link5"
		}]

	for(i = 0; i < ids.length; i++) {
		console.log(ids[i].div);
		$(ids[i].button).click(function() {
			$(ids[i].div).append('<form action="/profile/{{username}}" method="post">' +
									'<input type="text" name="link_number" hidden="true" value="link_1">' +
									'<input type="text" name="link_title" id="form_one_url">' +
									'<input type="text" name="link_url" id="form_one_title">' +
									'<input type="submit">' +
								'</form>');
		});
	}
});

	
