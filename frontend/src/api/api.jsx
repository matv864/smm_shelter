import React, { useState, useEffect } from "react";
import axios from "axios";

// api.interceptors.request.use((config) => {
//     config.headers.Authorization = `Bearer ${token}`
//     return config
// })

// axios.get(webApiUrl, { headers: {"Authorization" : `Bearer ${tokenStr}`} });
// axios.defaults.headers.common["Content-Type"] = "application/json";
// axios.defaults.headers.common['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ijk5OSIsImV4cCI6MTcxMjE0NTc0MH0.VXnnU4pr8Gc7GFViT77qvJN3eMJcsHyDww0JBeWBcuw';
// api.interceptors.request.use(
//     config => {
//       config.headers['Authorization'] = `Bearer ${'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ijk5OSIsImV4cCI6MTcxMjE0NTc0MH0.VXnnU4pr8Gc7GFViT77qvJN3eMJcsHyDww0JBeWBcuw'}`;
//           return config;
//       },
//       error => {
//           return Promise.reject(error);
//       }
// );
// const headers1 = { Authorization: `Bearer ${tokenStr}` };
// return axios.get(URLConstants.USER_URL, { headers });

let api = axios.create(
    {
        withCredentials: false,
        baseURL: `http://localhost:8002/`,
        headers: {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ijk5OSIsImV4cCI6MTcxMjI4OTA2MX0.gqX3ePgJj1RCnicL9ARQNLF1kBVJIafoq9oBbla5p3Y',
        }
    }
)

// let t = await fetch(webApiUrl, {
//   method: 'POST',
//   headers: {
//     'Accept': 'application/json',
//     'Authorization': `Bearer ${tokenStr}`
//   },
//   body: ''
// })
let webApiUrl = "http://localhost:8002/who_am_i"
let tokenStr = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ijk5OSIsImV4cCI6MTcxMjI4OTA2MX0.gqX3ePgJj1RCnicL9ARQNLF1kBVJIafoq9oBbla5p3Y"
export default function Test() {
  const [data, setData] = useState([]);
    useEffect(() => {
        fetch(webApiUrl, {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Authorization': `Bearer ${tokenStr}`
            },
            body: ''
          })
        .then((response) => response.json())
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
