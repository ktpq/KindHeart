import axios from "axios";
export async function load({cookies}){
    const base_api = import.meta.env.VITE_API_URL
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