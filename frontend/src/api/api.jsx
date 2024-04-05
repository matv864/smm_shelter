import React, { useState, useEffect } from "react";
import axios from "axios";

let tokenStr = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ijk5OSIsImV4cCI6MTcxMjI5MDM1N30.weYjRExSzVhK9K5RZDKDp_MWkkseqY6C1k1ZRhWG0aM"
let api = axios.create(
    {
        withCredentials: false,
        baseURL: `http://localhost:8002/`,
        headers: {
            'accept': 'application/json',
            'Authorization': `Bearer ${tokenStr}`
        }
    }
)

export default function Test() {
  const [data, setData] = useState([]);
    useEffect(() => {
        api.post('who_am_i')
        .then((res) => {
            setData(res);
        })
        .catch(err => {
            console.log(err)
        })
  },[]);
  console.log(data)
  return (
    <div>
      data
    </div>
  );
}




























































// get requests



// export const UsersApi = {
//     getCard(id = 1) {
//         return api.get('api/v1/get_card/' + id)
//         .then (response => response.data)
//         .catch((error) => {
//             console.log(error);
//           });
//     },
//     getListTypes() {
//         return api.get('/api/v1/list_types')
//         .then (response => response.data)
//         .catch((error) => {
//             console.log(error);
//           });
//     },
// }

// export default function Test() {
//   const [data, setData] = useState([]);
//   useEffect(() => {
//     api.post(`who_am_i`)
//       .then((data) => {
//         setData(data);
//       })
//   },[]);
//   console.log(data)
//   return (
//     <div>
//       data
//     </div>
//   );
// }

