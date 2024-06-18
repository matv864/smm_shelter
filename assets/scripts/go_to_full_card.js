var go_to_card = async function(card_id){
    let card_info = await get_card_data(card_id)
    console.log(card_info)

    let self_description = '<div class="back_button"><button onclick="location.reload();">назад</button></div>'
    self_description += `
        <div class="block-for-animalGreet">
            <p class="event-title">меня зовут - ${card_info.name}</p>
        </div>
    `

    self_description += `
        <div class="block-for-animalGreet">
            <p class="event-title">я ${card_info.gender}</p>
        </div>
    `

    self_description += `
        <div class="block-for-animalGreet">
            <p class="event-title">мне ${card_info.age}</p>
        </div>
    `

    self_description += `
        <div class="block-for-animalGreet">
            <p class="event-title">сейчас в ${card_info.status}</p>
        </div>
    `

    if (card_info.breed){
        self_description += `
            <div class="block-for-animalGreet">
                <p class="event-title">моя порода - ${card_info.breed}</p>
            </div>
        `
    }

    let text_pet = ""
    if (card_info.personality){
        text_pet += `<p class="event-title">${card_info.personality}</p>`
    }
    if (card_info.appearance){
        text_pet += `<p class="event-title">${card_info.appearance}</p>`
    }
    if (card_info.health){
        text_pet += `<p class="event-title">${card_info.health}</p>`
    }
    if (card_info.description){
        text_pet += `<p class="event-title">${card_info.description}</p>`
    }

    self_description += `<div class="block-for-animalGreet">${text_pet}</div>`
    
    html_images = ""
    card_info.images.forEach(path => {
        html_images += `<img src=${path} alt="pet_photo" class="img_photozone" />`
    });

    document.getElementById("main").innerHTML = `
        <div class="self-description">${self_description}</div>
        <div class="photozone">${html_images}</div>
    `
}