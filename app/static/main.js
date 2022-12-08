let modelDiv = document.getElementById("edit-modal")
let modal = new bootstrap.Modal(modelDiv)


let edit_task = (name, calories, url) => {
    modelDiv.querySelector("#edit-form").setAttribute("action", url)
    modelDiv.querySelector("#name").setAttribute("value", name)
    modelDiv.querySelector("#calories").setAttribute("value", calories)
    modal.show()
}