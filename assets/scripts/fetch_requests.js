const link = "http://31.200.237.168";


var get_image_link = async function(image_schema){
    let filename = image_schema.filename.split(".");
    let extension = filename[filename.length - 1];
    let database_filename = `${image_schema.id}.${extension}`
    let full_database_filename = `/storage/pets_images/${database_filename}`
    return full_database_filename;
}

var get_list_data = async function(){
    let request;
    let success = 0;
    for (var i = 0; i < 10; i++) {
        request = await fetch(`${link}/api/pets/list`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          })
        
          if (!request.ok) {
            console.log("bad request")
            continue
          } else {
            success = 1;
            break
          }
    }

    if (success){
        const res = [];
        // let image_array = [];
        let json = await request.json()
        // console.log(json)
        json.forEach(async function(body){
            // image_array = [];
            // body.images.forEach(async function(image_schema){
            //     image_array.push(await get_image_link(image_schema))
            // });
            res.push({
                "id": body.id,
                "name": body.name,
                "image": await get_image_link(body.images[0])
            })
        })
        return res;
    } else {
        console.log("trash")
    }
  }

var get_card_data = async function(card_id){
    let request;
    let success = 0;
    for (var i = 0; i < 10; i++) {
        request = await fetch(`${link}/api/pets/${card_id}`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          })
        
          if (!request.ok) {
            console.log("bad request")
            continue
          } else {
            success = 1;
            break
          }
    }

    if (success){
        const json = await request.json();
        let good_images = [];
        json.images.forEach(async function(block){
          good_images.push(await get_image_link(block))
        })
        json.images = good_images

        if (json.gender == "M"){
          json.gender = "мальчик"
        } else {
          json.gender = "девочка"
        }


        return json;
    } else {
        console.log("trash")
    }
}


