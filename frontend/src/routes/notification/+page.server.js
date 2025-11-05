import axios from "axios";
import { PRIVATE_API_URL } from "$env/static/private"
export async function load({cookies}){
    const base_api = PRIVATE_API_URL
    const token = cookies.get('authToken')
    try{
        const response = await axios.get(`${base_api}/api/notification/`, {
            headers: { Authorization: `Token ${token}`}
        })

        return {
            allNoti: response.data
        }
    } catch (error){
        console.log(error.message)
    }

}