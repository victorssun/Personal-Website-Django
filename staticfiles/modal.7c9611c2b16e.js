//TODO: make dynamic modal
function showModal(pk) {
//    var obj = {{ recipes |lookup:pk }};

//  document.getElementById("recipe-name").innerHTML = "recipe name " + pk;
    document.getElementById("recipe-name").innerHTML = "{{ test }}";

    document.getElementById("recipe-img").innerHTML = `<img src="/media/{{ recipe.img }}" width="250px">`

    document.getElementById("recipe-info").innerHTML = `
        <h5>{{ recipe.cuisine.cuisine_name }} {{ recipe.course.course_name }} dish: </h5>
        <p>{{ recipe.description }}</p>
        <h5>Ingredients:</h5>
        <p>{% for ingredient in recipe.ingredients.all %}
            <li>{{ ingredient.ingredient_name}}</li>
        {% endfor %}</p>`

    document.getElementById("recipe-footer").innerHTML = `
    {{ recipe.date_modified.date_modified }} <br>
    <a class="btn btn-light btn-sm" href="/recipes/{{ recipe.slug }}" role="button">Go to</a>`
}
