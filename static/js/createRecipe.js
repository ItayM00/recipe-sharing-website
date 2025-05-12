
const title = document.querySelector("#title");
const category = document.querySelector("#categorySelect");
const description = document.querySelector("#description");
const instructions = document.querySelector("#instructions");


// function to summerize all the ingredients rows to 
// 2 seperate list for easier storage in the database
function summarizeIngredients() {
    let ingredients = [];
    let sizes = [];

    // Select all ingredient rows
    document.querySelectorAll(".ingredientChoose").forEach(row => {
        let ingredientName = row.querySelector("input[name='ingredients']").value;
        let quantity = row.querySelector("input[name='count']").value;
        let size = row.querySelector("select[name='sizes']").value;

        if (ingredientName && quantity && size) {
            ingredients.push(ingredientName);
            sizes.push(`${quantity} ${size}`);
        }
        else{
            window.alert("please fill out all the ingredients");
            return {}
        }
    });

    console.log("Ingredients:", ingredients);
    console.log("Sizes:", sizes);

    return { ingredients, sizes };
}

// function to send the recipe data through the API to backend
function sendData() {
    let summary = summarizeIngredients();

    if (!summary) {
        return;
    }

    dataObj = {
        'title': title.value,
        'category': category.value.toLowerCase(),
        'ingredients': summary.ingredients,
        'sizes': summary.sizes,
        'description': description.value,
        'instructions': instructions.value,
        'likes': 0,
        'comments': []
    }

    fetch('/create-recipe', {  // route to send data
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Specify JSON data
        },
        body: JSON.stringify(dataObj)  // Convert JS object to JSON
    })
    .then(response => {
        if (response.redirected) {
            // If the response contains a redirect, follow it manually
            window.location.href = response.url;
        } else if (response.ok) {
            return response.text();
        } else {
            return response.json();
        }
    })
    .then(data => {
        console.log('Response from Flask:', data);  // Handle response if needed (e.g., error message)
    })
    .catch(error => {
        console.error('Error:', error);  // Handle any errors that might occur during the fetch
    });
}



// function to dynamiclly add a line for a new ingredient
function addIngredient(){
    let list = document.querySelector(".ingredientsList"); // Parent div

    // Create new ingredient container
    let newDiv = document.createElement("div");
    newDiv.classList.add("ingredientChoose");

    // Create ingredient input
    let newIngredient = document.createElement("input");
    newIngredient.classList.add("ingredient-input");
    newIngredient.type = "text";
    newIngredient.name = "ingredients";
    newIngredient.placeholder = "Ingredient name";

    // Create count input
    let newCount = document.createElement("input");
    newCount.classList.add("amount-input");
    newCount.type = "number";
    newCount.name = "count";
    newCount.placeholder = "amount";

    // Create size dropdown
    let newSizeSelect = document.createElement("select");
    newSizeSelect.classList.add("sizes-select");
    newSizeSelect.name = "sizes";

    let options = ["gram", "cup", "kg", "oz", "ml", "L"];
    options.forEach(size => {
        let option = document.createElement("option");
        option.value = size;
        option.textContent = size;
        newSizeSelect.appendChild(option);
    });

    let newDelbt = document.createElement("button");
    newDelbt.classList.add("delete-bt");
    newDelbt.addEventListener("click", () => removeIngredient(newDelbt));
    newDelbt.innerText = "✖";

    // Append inputs to newDiv
    newDiv.appendChild(newIngredient);
    newDiv.appendChild(newCount);
    newDiv.appendChild(newSizeSelect);
    newDiv.appendChild(newDelbt);

    // Append new ingredient div to the main container
    list.appendChild(newDiv);
}

function removeIngredient(button) {
    const ingredientDiv = button.closest('.ingredientChoose');
    if (ingredientDiv) {
        ingredientDiv.remove();
    }
}
