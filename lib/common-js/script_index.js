function getArticles() {
    $.get('/get_articles_index', function(data) {
        console.log(data);
        var article_names = []
        var article_authors = []
        var article_dates = []
        for (var i=0; i<data.length; i++) {
            article_names.push(data[i][0]);
        }
        for (var i=0; i<data.length; i++) {
            article_authors.push(data[i][1]);
        }
        for (var i=0; i<data.length; i++) {
            article_dates.push(data[i][2]);
        }
        console.log(article_names);
        console.log(article_authors);
        console.log(article_dates);

        for (var k=0; k<article_names.length; k++){
            console.log(article_names[k])
//            $('#article_name_'+k).html(article_names[k]);
               $('#article_name_'+k).html("<a href=/article_"+ k +">"+"<b>"+article_names[k]+"</a>"+"</b>");
        }
        for (var k=0; k<article_authors.length; k++){
            console.log(article_authors[k])
            $('#article_author_'+k).html(article_authors[k]);
        }
        for (var k=0; k<article_dates.length; k++){
            console.log(article_dates[k])
            $('#article_date_'+k).html(article_dates[k]);
        }

    });
}

$(document).ready(function() {
    getArticles();
});
