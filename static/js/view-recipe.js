let postBt = document.getElementById("post-bt");
let commentText = document.getElementById("comment-text");

const recipeId = document.getElementById('recipe-id').value;
const userId = document.getElementById('user-id').value;

postBt.addEventListener('click', () => {
    if(!commentText.value) return;

    comment = {
        recipe_id: recipeId,
        author_id: userId,
        text: commentText.value
    };

    console.log(comment);

    fetch(`/recipes/${recipeId}/comments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Specify JSON data
        },
        body: JSON.stringify(comment)  // Convert JS object to JSON
    })
    .then(response => response.json())
    .then(res => {
        if(res.success) { commentText.value = ""; alert(res.success); }
        else if(res.error) alert(res.error);
    })
    .catch(error => console.log('error: ' + error));
});