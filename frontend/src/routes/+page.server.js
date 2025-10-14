import axios from "axios";


export async function load({ params, cookies }) {
    const base_api = import.meta.env.VITE_API_URL;
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