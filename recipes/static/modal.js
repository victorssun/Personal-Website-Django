function show_modal(slug) {

    $.ajax({
        url: "/recipes/" + slug + "/json",
        type: 'GET',
        dataType: 'json',
        success: function(resp) {
            var recipe_info = "";

            document.getElementById("recipe-name").innerHTML = resp['name'];
            document.getElementById("recipe-img").innerHTML = "<img src='/media/" + resp['img'] + "' width='250px'>"

            recipe_info = recipe_info + "<h5>" + resp['cuisine'] + " " + resp['course'] + " dish: </h5>"
            recipe_info = recipe_info + "<p>" + resp['description'] + "</p>"
            recipe_info = recipe_info + "<h5> Ingredients: </h5>"
            recipe_info = recipe_info + "<p>"
            for (const key in resp['ingredients']) {
                recipe_info = recipe_info + "<li>" + resp['ingredients'][key] + "</li>"
            }
            recipe_info = recipe_info + "</p>"
            document.getElementById("recipe-info").innerHTML = recipe_info

            document.getElementById("recipe-footer").innerHTML = resp['date_modified'] + "<br> <a class='btn btn-light btn-sm' href='/recipes/" + resp['slug'] + "' role='button'>Go to</a>"
        },
        error: function(xhr, status, error) {
            document.getElementById("recipe-info").innerHTML = xhr.status + ": " + xhr.responseText;
        }
    });
}
