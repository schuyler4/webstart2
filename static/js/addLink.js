$(document).ready(function() {
	function editOne(button, div, value) {
		$(button).click(function() {
			$(div).append('<form action="/profile/{{username}}" method="post">' +
			'<input type="text" name="link_number" hidden="true" value=' + value + '>' +
			'<input type="text" name="link_title" id="form_one_url">' +
			'<input type="text" name="link_url" id="form_one_title">' +
			'<input type="submit">' +
			'</form>');
		});
	}
	editOne('#editLinkOne', '#link1', "link_1");
	editOne('#editLinkTwo', '#link2', "link_2");
	editOne('#editLinkThree', '#link3', "link_3");
	editOne('#editLinkFour', '#link4', "link_4");
	editOne('#editLinkFive', '#link5', "link_5");
});