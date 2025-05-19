let recipesHolder = document.querySelector(".main-content");
let filtersButtons = document.querySelectorAll(".navigation button");
let searchBt = document.getElementById("search-bt");
let searchInput = document.querySelector(".search-input");

filtersButtons.forEach(child => {
    child.addEventListener('click', () => {
        changeCategory(child);
        getRecipes('category', child.innerHTML.toLowerCase().replace(' ', ''))
    })
});

searchBt.addEventListener('click', () => {
    if(!searchInput.value) return;

    getRecipes('title', searchInput.value.toLowerCase());
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
            <a class="card" href="/recipes/${recipe._id}">
                <img src="${recipe.picture}" alt="recipe pic">
                <h2>${recipe.title}</h2>
                <div class="desc">
                    <div class="creator">${recipe.creator_name}</div>
                    <div class="likes">${recipe.likes}👍</div>
                </div>
            </a>
            `;
        recipesHolder.appendChild(recipeElement);
    });
}

function changeCategory(curButton){
    filtersButtons.forEach(button => {
        button.classList.remove("category-on");
    });
    curButton.classList.add("category-on");
}

setTimeout(() => {
    getRecipes();
}, 500);