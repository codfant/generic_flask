function read_meta_tag() {
    var meta_json_array = JSON.parse(document.getElementById("javascript_array").getAttribute("meta_tag"))
    var animal_dropdown = document.getElementById("animal_dropdown");
    var option = document.createElement("option");
    option.text = "Bear";
    option.value = "Roar!";
    option.id = "Bear";
    animal_dropdown.add(option);
        for (var i in meta_json_array) {
            console.log(i)
            console.log(meta_json_array[i])
            var option = document.createElement("option");
            option.text = i;
            option.value = meta_json_array[i];
            option.id = i;
            animal_dropdown.add(option);
    }
}