
var originalToOptions = Array.from(document.getElementById("to").options);
console.log(originalToOptions);
function updateOptions() {
    
    var toSelect = document.getElementById("to");

    toSelect.innerHTML = "";
    originalToOptions.forEach(function (option) {
        toSelect.add(option.cloneNode(true));
    });
    var stopsArray=originalStopkm;
    var fromSelect = document.getElementById("from");
    var selectedOption = fromSelect.options[fromSelect.selectedIndex].text;

    var found = false;
    for (var i = 0; i < toSelect.options.length; i++) {
        if (toSelect.options[i].text === selectedOption) {
            found = true;
            toSelect.remove(i);
        }

        if (!found) {
            toSelect.remove(i);
            i--;
        }

        if (!found && i == toSelect.options.length - 1) {
            originalToOptions.forEach(function (option) {
                toSelect.add(option.cloneNode(true));
            });
            stopsArray=originalStopkm;
            break;
        }
       
    }
    
 console.log("welocome");


}
