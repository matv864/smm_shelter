
var make_list_pets = async function(){
    let list_data = await get_list_data();

    inner_html = '';

    list_data.forEach(function(pet_data){
        inner_html += `<div class="block-for-animalHelp"><img
          src="${pet_data.image}"
          alt="img-for-help-animals"
          class="img_card"
        />
        <p class="event-title">${pet_data.name}</p>
        <button class="btn want-help-btn">Помочь</button>
        <button class="btn want-help-btn" onclick="go_to_card('${pet_data.id}')">познакомиться</button>
      </div>`
    })
    
    document.getElementById("main").innerHTML = inner_html;
}