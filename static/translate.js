document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("translateButton").addEventListener("click", function() {
        var sentence = document.getElementById("sentence").value;
        var sourceLang = document.getElementById("sourceLang").value;
        var targetLang = document.getElementById("targetLang").value;

        var apiUrl = '/translate';

        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'sentence': sentence,
                'sourceLang': sourceLang,
                'targetLang': targetLang,
            }),
        })
        .then(response => response.json())
        .then(data => {
            var translation = data.translation;
            document.getElementById("translationResult").textContent = translation;
        })
        .catch(error => {
            console.error('Translation error:', error);
        });
    });
});
