import axios from "axios"
export async function load({params, cookies}){
    const base_api = import.meta.env.VITE_API_URL
    const token = cookies.get('authToken');
    const userResponse = await axios.get(`${base_api}/api/user/${params.id}/`, {
        headers: {Authorization: `Token ${token}`}
    })

    const eventResponse = await axios.get(`${base_api}/api/event/owner/${params.id}/`, {
        headers: { Authorization: `Token ${token}`}
    })

    return {
        user: userResponse.data,
        events: eventResponse.data
    }
}