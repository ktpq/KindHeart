import axios from "axios";
import { PRIVATE_API_URL } from "$env/static/private";
export async function load({ cookies }) {
    try{    
        const token = cookies.get('authToken')
        const base_api = PRIVATE_API_URL
        const response = await axios.get(`${base_api}/api/participation/`, {
            headers: {
                Authorization: `Token ${token}`
            }
        })

        return {
            allEvent: response.data
        }
    } catch (error){
        console.log(error.message)
    }
}