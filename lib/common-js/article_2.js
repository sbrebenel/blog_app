var page;
$.get("/get_comments_article_2", function(data){
    page = data;
    console.log(page);
});


function postComment(){
    $('#button_post_comment').on('click', function replaceWords(e) {
        e.preventDefault();
        var selected_name = $('#comment_name').val();
        var selected_email = $('#comment_email').val();
        var selected_text = $('#comment_text').val();
        var badWords = ["lgbt","2g1c","2 girls 1 cup","acrotomophilia","alabama hot pocket","alaskan pipeline","anal",
        "anilingus","anus","apeshit","arsehole","ass","asshole","assmunch","auto erotic","autoerotic","babeland",
        "baby batter","baby juice","ball gag","ball gravy","ball kicking","ball licking","ball sack","ball sucking",
        "bangbros","bareback","barely legal","barenaked","bastard","bastardo","bastinado","bbw","bdsm","beaner",
        "beaners","beaver cleaver","beaver lips","bestiality","big black","big breasts","big knockers","big tits",
        "bimbos","birdlock","bitch","bitches","black cock","blonde action","blonde on blonde action","blowjob",
        "blow job","blow your load","blue waffle","blumpkin","bollocks","bondage","boner","boob","boobs","booty call",
        "brown showers","brunette action","bukkake","bulldyke","bullet vibe","bullshit","bung hole","bunghole","busty",
        "butt","buttcheeks","butthole","camel toe","camgirl","camslut","camwhore","carpet muncher","carpetmuncher",
        "chocolate rosebuds","circlejerk","cleveland steamer","clit","clitoris","clover clamps","clusterfuck","cock",
        "cocks","coprolagnia","coprophilia","cornhole","coon","coons","creampie","cum","cumming","cunnilingus","cunt",
        "darkie","date rape","daterape","deep throat","deepthroat","dendrophilia","dick","dildo","dingleberry",
        "dingleberries","dirty pillows","dirty sanchez","doggie style","doggiestyle","doggy style","doggystyle",
        "dog style","dolcett","domination","dominatrix","dommes","donkey punch","double dong","double penetration",
        "dp action","dry hump","dvda","eat my ass","ecchi","ejaculation","erotic","erotism","escort","eunuch","faggot",
        "fecal","felch","fellatio","feltch","female squirting","femdom","figging","fingerbang","fingering","fisting",
        "foot fetish","footjob","frotting","fuck","fuck buttons","fuckin","fucking","fucktards","fudge packer",
        "fudgepacker","futanari","gang bang","gay sex","genitals","giant cock","girl on","girl on top",
        "girls gone wild","goatcx","goatse","god damn","gokkun","golden shower","goodpoop","goo girl","goregasm",
        "grope","group sex","g-spot","guro","hand job","handjob","hard core","hardcore","hentai","homoerotic","honkey",
        "hooker","hot carl","hot chick","how to kill","how to murder","huge fat","humping","incest","intercourse",
        "jack off","jail bait","jailbait","jelly donut","jerk off","jigaboo","jiggaboo","jiggerboo","jizz","juggs",
        "kike","kinbaku","kinkster","kinky","knobbing","leather restraint","leather straight jacket","lemon party",
        "lolita","lovemaking","make me come","male squirting","masturbate","menage a trois","milf",
        "missionary position","motherfucker","mound of venus","mr hands","muff diver","muffdiving","nambla","nawashi",
        "negro","neonazi","nigga","nigger","nig nog","nimphomania","nipple","nipples","nsfw images","nude","nudity",
        "nympho","nymphomania","octopussy","omorashi","one cup two girls","one guy one jar","orgasm","orgy",
        "paedophile","paki","panties","panty","pedobear","pedophile","pegging","penis","phone sex","piece of shit",
        "pissing","piss pig","pisspig","playboy","pleasure chest","pole smoker","ponyplay","poof","poon","poontang",
        "punany","poop chute","poopchute","porn","porno","pornography","prince albert piercing","pthc","pubes","pussy",
        "queaf","queef","quim","raghead","raging boner","rape","raping","rapist","rectum","reverse cowgirl","rimjob",
        "rimming","rosy palm","rosy palm and her 5 sisters","rusty trombone","sadism","santorum","scat","schlong",
        "scissoring","semen","sex","sexo","sexy","shaved beaver","shaved pussy","shemale","shibari","shit","shitblimp",
        "shitty","shota","shrimping","skeet","slanteye","slut","s&m","smut","snatch","snowballing","sodomize","sodomy",
        "spic","splooge","splooge moose","spooge","spread legs","spunk","strap on","strapon","strappado","strip club",
        "style doggy","suck","sucks","suicide girls","sultry women","swastika","swinger","tainted love","taste my",
        "tea bagging","threesome","throating","tied up","tight white","tit","tits","titties","titty","tongue in a",
        "topless","tosser","towelhead","tranny","tribadism","tub girl","tubgirl","tushy","twat","twink","twinkie",
        "two girls one cup","undressing","upskirt","urethra play","urophilia","vagina","venus mound","vibrator",
        "violet wand","vorarephilia","voyeur","vulva","wank","wetback","wet dream","white power","wrapping men",
        "wrinkled starfish","xx","xxx","yaoi","yellow showers","yiffy","zoophilia","kill"];

        var censored = censore(selected_text, badWords);
        selected_text = censored;
        console.log(censored);
        $('#comment_text').val(censored);

        var remove_links = censored.replace(/^(\[url=)?(http?:\/\/)?(https?:\/\/)?(www\.|\S+?\.)(\S+?\.)?\S+$\s*/mg, '');
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

        $.post('/post_comment_two', {com_name: selected_name, com_email: selected_email, com_text: remove_links}, function(data) {
            console.log(data);
        });
        $.confirm({
            title: "Info",
            content: "Your comment is being analysed! We'll post in short time! Thank you!",
            buttons: {
                ok : {
                    text : 'OK',
                    btnClass : 'btn-green',
                    keys: ['enter','esc'],
                    action: function(){
                        setTimeout(function(){window.location.reload();},10);
                    }
                }
            }
        });
        $("form").trigger("reset");
    });
}

function getMostCommonWords() {
    $('#button_common_words').on('click', function() {
    $.dialog({
        columnClass: "col-md-6 col-md-offset-3",
        title: 'Info',
        content: "We are searching the most common words used in our comments! The result of searching will be displayed in short time!",
    });
    $.get('/get_most_common_words_two', function (data) {
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

function sentimentAnalyze() {
    $('#button_sentiment_analyze').on('click', function() {
        $.dialog({
            columnClass: "col-md-6 col-md-offset-3",
            title: 'Info',
            content: "Comments are being analyzed! The result of sentiment analyze will be displayed in short time!",
        });
        $.get('/get_sentiment_analyze_article_2', function(data) {
            var sentiment_score = [];
            for (var i = 0; i < data.length; i+=3){
		    sentiment_score.push(data.slice(i,i+3));
		    }
		    console.log(sentiment_score);
		    for (var j = 0; j < sentiment_score.length ;  j++){
		        var arr_sentiment_score = [];
		        arr_sentiment_score.push(sentiment_score[j][0]);
		        arr_sentiment_score.push(sentiment_score[j][1]);
		        arr_sentiment_score.push(sentiment_score[j][2]);

		        function indexOfMax(arr) {
                    if (arr.length === 0) {
                    return -1;
                    }
                    var max = arr[0];
                    var maxIndex = 0;
                    for (var i = 1; i < arr.length; i++) {
                        if (arr[i] > max) {
                        maxIndex = i;
                        max = arr[i];
                        }
                    }
                    return maxIndex;
                }

                maxValue = Math.max.apply(this, arr_sentiment_score);
		        position_maxValue = indexOfMax(arr_sentiment_score);

		        if(position_maxValue === 0){
		            $('#sentiment_result_'+j).html("<h4><b><font color='#d82222'>Result : Negative comment!</h4></b></font>");
		        } else if (position_maxValue === 1){
		            $('#sentiment_result_'+j).html("<h4><b><font color='#67a52c'>Result : Positive comment!</h4></b></font>");
		        } else{
		            $('#sentiment_result_'+j).html("<h4><b><font color='#feb953'>Result : Neutral comment!</h4></b></font>");
		        }

		        var data_sentiment_score = [{
		            x : ['Negative','Positive','Neutral'],
		            y : arr_sentiment_score,
		            marker: {color: ['rgb(216, 34, 34)', 'rgb(103, 165, 44)','rgb(254, 185, 83)']},
		            type : 'bar',
		        }];

		        var layout = {
		            title: 'Sentiment Analyze Score'
		        };

		        Plotly.newPlot('sentiment_score_'+j, data_sentiment_score, layout);
		    }
        });
    });
}

function entityAnalyze() {
    function launchAnalysis() {
        $.dialog({
            columnClass: "col-md-6 col-md-offset-3",
            title: 'Info',
            content: "Comments are being analyzed! The result of entity analyze will be displayed in short time!",
        });
        //Extract text to analyse
        jQuery.each(page, function(index, value) {
            var $textEditor_index = $('#'+parseInt(index+1));
            console.log($textEditor_index);
            var toAnalyse_index = $textEditor_index.text();
            extractAnnotations(toAnalyse_index, function(err, result) {
        if (!err) {
            //Insert formatted result into the editor
            $textEditor_index.html(annotationsToHml(result));
        } else {
            if (console.log)
                console.log('Error while doing annotations extraction: ' + err);
            }
        });
    });
}

    // Function to call the SYSTRAN NLP Api extractAnnotations
  function extractAnnotations(content, callback) {
    $.ajax({
      method:'GET',
      url: 'https://api-platform.systran.net/nlp/ner/extract/annotations?key=d55c734f-0d38-4dff-8310-d5478dc89f17&lang=en',
      data: {
        input: content
      },
      success: function(data) {
        callback(null, data);
      },
      error: function(xhr, status, err) {
        callback(err);
      }
    });
  }

  // Get css class from annotation type
  function classFromAnnotationType(type) {
    if (type) {
      if (type.search(/^ENAMEX_(firstname|lastname|person)|title/) !== -1)
        return 'people';
      else if (type.search(/^ENAMEX_organization/) !== -1)
        return 'organization';
      else if (type.search(/^ENAMEX_location/) !== -1)
        return 'location';
      else if (type.search(/TIMEX|day|month|year/) !== -1)
        return 'time';
    }
    return '';
  }

  // Function to build html from the result returned by the extractAnnotations api
  function annotationsToHml(annotations) {
    var html = '';
    var i, j, li, lj;
    if (annotations && annotations.annotations) {
      for (i = 0, li = annotations.annotations.length; i < li; ++i) {
        var annotation = annotations.annotations[i];
        if (annotation.entities) {
          var spans = [];
          var lastIdx = 0;
          for (j = 0, lj = annotation.entities.length; j < lj; ++j) {
            var entity = annotation.entities[j];
            spans.push({idx: entity.start, value: '<span class="entity highlight ' + classFromAnnotationType(entity.type) + '">', start: true});
            spans.push({idx: entity.end, value: '</span>'});
          }
          spans.sort(function(a,b) {
            if (a.idx === b.idx) {
              return a.start ? (b.start ? 0 : 1) : (b.start ? -1: 0);
            } else {
              return (a.idx < b.idx) ? -1: 1;
            }
          });
          for (j = 0, lj = spans.length; j < lj; ++j) {
            var span = spans[j];
            html += annotation.source.substring(lastIdx, span.idx) + span.value;
            lastIdx = span.idx;
          }
          html += annotation.source.substring(lastIdx);
        } else {
          html += annotation.source;
        }
        html += '<br>';
      }
    }
    return html;
  }
  $('#button_entity').click(launchAnalysis);
}

function emotionAnalyze() {
    $('#button_emotion_analyze').on('click', function() {
        $.dialog({
            columnClass: "col-md-6 col-md-offset-3",
            title: 'Info',
            content: "Comments are being analyzed! The result of emotion analyze will be displayed in short time!",
        });
        $.get('/get_emotion_analyze_article_2', function(data) {
            var emotion_score = [];
            for (var i = 0; i < data.length; i+=5){
		    emotion_score.push(data.slice(i,i+5));
		    }
		    console.log(emotion_score);
		    for (var j = 0; j < emotion_score.length ;  j++){
		        var arr_emotion_score = [];
		        arr_emotion_score.push(emotion_score[j][0]); // anger value
		        arr_emotion_score.push(emotion_score[j][1]); // surprise value
		        arr_emotion_score.push(emotion_score[j][2]); // sadness value
		        arr_emotion_score.push(emotion_score[j][3]); // fear value
		        arr_emotion_score.push(emotion_score[j][4]); // joy value

		        var data_emotion_score = [{
		            values : arr_emotion_score,
		            labels : ['Anger','Surprise','Sadness', 'Fear', 'Joy'],
		            marker: {colors: ['rgb(216, 34, 34)', 'rgb(247, 218, 29)','rgb(58, 134, 234)','rgb(52, 53, 56)','rgb(3, 188, 71)']},
		            type : 'pie',
		        }];

		        var layout = {
		            title: 'Emotion Analyze Score'
		        };

		        Plotly.newPlot('emotion_score_'+j, data_emotion_score, layout);
		    }
        });
    });
}

function generateComments() {
    $('#button_generate_comments').on('click', function() {
        $.get('/generate_comments_2', function(data) {
            $.confirm({
            title: "Info",
            content: data,
            buttons: {
                confirm: function () {
                    setTimeout(function(){window.location.reload();},10);
                    }
                }
            });
        });
    });
}

$(document).ready(function() {
    postComment();
    getMostCommonWords();
    sentimentAnalyze();
    entityAnalyze();
    emotionAnalyze();
    generateComments();
});