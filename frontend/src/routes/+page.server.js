import axios from "axios";

import { PRIVATE_API_URL } from "$env/static/private";
export async function load({ params, cookies }) {
    const base_api = PRIVATE_API_URL;
    const token = cookies.get("authToken");
    try{
        if (token){
            const response = await axios.get(`${base_api}/api/event/canjoin/`, {
                headers: { Authorization: `Token ${token}`}
            })
            return {
                allEvent: response.data,
                isLogin: true
            }
        } else {
            return {
                allEvent: [],
                isLogin: false
            }
        }
    } catch (error){
        console.log(error.message)
    }
    
}