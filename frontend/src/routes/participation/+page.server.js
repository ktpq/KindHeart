import axios from "axios";

export async function load({ cookies }) {
    try{    
        const token = cookies.get('authToken')
        const base_api = import.meta.env.VITE_API_URL
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