import axios from "axios"
// import Cookies from "js-cookie";

export async function load({ params, cookies }) {
    const base_api = import.meta.env.VITE_API_URL;
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