import axios from "axios";


export async function load({ params, cookies }) {
    const base_api = import.meta.env.VITE_API_URL;
    const token = cookies.get("authToken");
    try{
        const response = await axios.get(`${base_api}/api/event/`, {
            headers: { Authorization: `Token ${token}`}
        })
        return {
            allEvent: response.data
        }
    } catch (error){
        console.log(error.message)
    }
    
}