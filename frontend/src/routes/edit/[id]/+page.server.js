import axios from "axios"
import { PRIVATE_API_URL } from "$env/static/private";
// import Cookies from "js-cookie";

export async function load({ params, cookies }) {
    const base_api = PRIVATE_API_URL;
    const token = cookies.get("authToken");
    try{
        const response = await axios.get(`${base_api}/api/event/${params.id}/`, {
            headers: {
                Authorization: `Token ${token}`
            }
        })
        return {
            event: response.data,
            id: params.id
        }
    } catch (error){
        console.log(error.message)
    }

}