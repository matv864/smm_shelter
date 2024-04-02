import React, { useEffect, useState } from "react";
import axios from "axios";

const access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkVnb3IiLCJleHAiOjE3MTIwNDEyMzR9.mjJ79mTNLYuy0NuE0LHAXTjBQmD2pWuQ51Z93DNSgkc"
export default function Test() {
  const [data, setData] = useState([]);
  axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
  useEffect(() => {
    axios
      .get("http://localhost:8002/who_am_i")
      .then((response) => {
        setData(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  console.log(data)
  return (
    <div>
      <h1>Data</h1>
    </div>
  );
}

// function Test() {
//   const [data, setData] = useState({ name: "", passwd: "" });
//   const [response, setResponse] = useState("");

//   const handleChange = (event) => {
//     setData({ ...data, [event.target.name]: event.target.value });
//   };

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     axios
//       .post("http://localhost:8002/login", data, {headers: {"Authorization" : `Bearer ${access_token}`}})
//       .then((response) => {
//         setResponse(response.data);
//       })
//       .catch((error) => {
//         console.log(error);
//       });
//   };

//   return (
//     <div>
//       <h1>Отправка данных на сервер</h1>
//       <form onSubmit={handleSubmit}>
//         <label>
//           Имя:
//           <input
//             type="text"
//             name="name"
//             value={data.name}
//             onChange={handleChange}
//           />
//         </label>
//         <br />
//         <label>
//           passwd:
//           <input
//             type="text"
//             name="passwd"
//             value={data.passwd}
//             onChange={handleChange}
//           />
//         </label>
//         <br />
//         <button type="submit">Отправить</button>
//       </form>
//       {response && (
//         <p>
//           Данные успешно отправлены: {response.name} ({response.passwd})
//         </p>
//       )}
//     </div>
//   );
// }

// export default Test;