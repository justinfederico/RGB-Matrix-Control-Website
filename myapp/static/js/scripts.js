$(document).ready(function() {
	/*--- Mouse ---*/
	$(document).on("mousemove", function(event) {
		var mouseX = event.pageX,
		    mouseY = event.pageY
		$(".mouse").css({
      "left": mouseX,
      "top": mouseY
    });
	});

	/*--- Link : background ---*/
	$(".link").on("mousemove", function(event) {
		var offset = $( this ).offset();
		var mouseX = event.pageX - offset.left,
		    mouseY = event.pageY - offset.top
		$(".link span").css({
      "left": mouseX,
      "top": mouseY
    });
	});

	/*--- Link : hover ---*/
	$(".link").hover(
		function() {
			$(".mouse").addClass("mouse-link")
		},

		function() {
			$(".mouse").removeClass("mouse-link")
		}
	);

	/*--- Link : click ---*/
	$(".link").click(function() {
		$(".mouse").addClass("mouse-clicked"),
		setTimeout(resetClick, 700)
	});

	function resetClick() {
		$(".mouse").removeClass("mouse-clicked")
	}
});
