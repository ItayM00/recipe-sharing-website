let recipesHolder = document.querySelector(".main-content");
let filtersButtons = document.querySelectorAll(".navigation button");

filtersButtons.forEach(child => {
    child.addEventListener('click', () => {
        changeCategory(child);
        getRecipes('category', child.innerHTML.toLowerCase().replace(' ', ''))
    })
});

function getRecipes(filterType = null, filterValue = null){
    recipesHolder.innerHTML = "";

    let url = "api/recipes";
    if (filterValue && filterValue !== 'all' && filterType) {
        url += `?${filterType}=${encodeURIComponent(filterValue)}`;
    }
    
    fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        populateRecipes(data);
    })
    .catch(error => console.log("error : " + error));
}

function populateRecipes(recipes){
    recipes.forEach(recipe => {
        const recipeElement = document.createElement('div');
        recipeElement.classList.add('recipe-card');
        recipeElement.innerHTML = `
            <img src="" alt="${recipe.title}">
            <h2>${recipe.title}</h2>
            <div>${recipe.description}</div>
            `;
            // <div>${recipe.likes}👍</div>
        recipesHolder.appendChild(recipeElement);
    });
}

function changeCategory(curButton){
    filtersButtons.forEach(button => {
        button.classList.remove("category-on");
    });
    curButton.classList.add("category-on");
}