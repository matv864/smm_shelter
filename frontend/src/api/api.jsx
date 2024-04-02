import React from "react";

// export default class ApiComponent extends React.Component {
//     constructor(props) {
//         super(props)
//         this.state = {
//             error: null,
//             isLoaded: false,
//             items: []
//         }
//     }

//     componentDidMount(){
//         fetch("http://localhost:8002/api/v1/get_card/1")
//         .then(res => res.json())
//         .then(
//             (result) => {
//                 this.setState({
//                     isLoaded: true,
//                     items: result
//                 })
//             },
//             (error) => {
//                 this.setState({
//                     isLoaded: true,
//                     error
//                 })
//             }
//         )
//     }
//     render(){
//         const {error, isLoaded, items} = this.state
//         if (error){
//             return <p>Error {error.message}</p>
//         }
//         else if (!isLoaded) {
//             return <p>Loading... </p>
//         }
//         else{
//             return (
//                 <div>
//                     {items}
//                 </div>
//             )
//         }
//     }
// }

import axios from "axios";

let instance = axios.create(
    {
        withCredentials: true,
        baseURL: `http://localhost:8002/`
    }
)

export const UsersApi = {
    // getUsers(currentPage = 1, pageSize = 10) {
    //     return instance.get(`users?page=${currentPage}&count=${pageSize}`)
    //     .then (response => response.data)
    // },
    // Unfollow(userId = 0) {
    //     return instance.delete(`follow/${userId}`)
    //     .then (response => response.data)
    // },
    // Follow(userId = 0) {
    //     return instance.post(`follow/${userId}`)
    //     .then (response => response.data)
    // },
    // authMe() {
    //     return instance.get('auth/me').then(response => response.data)
    // },
    // getProfile(userId) {
    //     return instance.get('profile/' + userId).then(response => response.data)
    // }
    petType(){
        return instance.get(`api/v1/list_types`)
    }
}