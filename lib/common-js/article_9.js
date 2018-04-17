function postComment(){
    $('#button_post_comment').on('click', function replaceWords(e) {
        e.preventDefault();
        var selected_name = $('#comment_name').val();
        var selected_email = $('#comment_email').val();
        var selected_text = $('#comment_text').val();
        var badWords = ["gay", "sex", "porno", "pula", "pizda", "lgbt", "mort"];

        var censored = censore(selected_text, badWords);
        selected_text = censored;
        console.log(censored);
        $('#comment_text').val(censored);

        var remove_links = censored.replace(/^(\[url=)?(https?:\/\/)?(www\.|\S+?\.)(\S+?\.)?\S+$\s*/mg, '');
        console.log(remove_links);
        $('#comment_text').val(remove_links);

        function censore(string, filters) {
            // "i" is to ignore case and "g" for global
            var regex = new RegExp(filters.join("|"), "gi");
            return string.replace(regex, function (match) {
            //replace each letter with a star
            var stars = '';
            for (var i = 0; i < match.length; i++) {
                stars += '*';
            }
            return stars;
            });
        }

        $.post('/post_comment_nine', {com_name: selected_name, com_email: selected_email, com_text: remove_links}, function(data) {
            console.log(data);
        });
        alert('Your comment has been posted! Thank you!');
        $("form").trigger("reset");
    });
}

function getMostCommonWords() {
    $('#button_common_words').on('click', function() {
    $.get('/get_most_common_words_nine', function (data) {
		var words = [];
		var no_words_app = [];
		console.log(data);
		for (var i = 0; i < data.length; i++) {
            words.push(data[i][0]);
            no_words_app.push(data[i][1]);
        }
        var data_most_common_words = [
		{
		    x: words,
		    y: no_words_app,
		    type: 'bar'
		}
		];
		var layout = {
		    title : "Most Common Words",
		};
		Plotly.newPlot('graph_most_common_words', data_most_common_words, layout);
        });
  });
}

$(document).ready(function() {
    postComment();
    getMostCommonWords();
});