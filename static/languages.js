document.addEventListener('DOMContentLoaded', function() {
    var languages =
                [
                    { "code": "en", "name": "English" },
                    { "code": "fr", "name": "French" },
                    { "code": "de", "name": "German" },
                    { "code": "hi", "name": "Hindi" },
                    { "code": "it", "name": "Italian" },
                    { "code": "zu", "name": "Zulu" }
                ];


    function populateLanguageOptions(selectId, languageArray) {
        var select = document.getElementById(selectId);
        for (var i = 0; i < languageArray.length; i++) {
            var option = document.createElement("option");
            option.value = languageArray[i].code;
            option.text = languageArray[i].name;
            select.appendChild(option);
        }
    }

    populateLanguageOptions('sourceLang', languages);
    populateLanguageOptions('targetLang', languages);
});