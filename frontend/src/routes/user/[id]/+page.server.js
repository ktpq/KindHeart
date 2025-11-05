import axios from "axios"

import { PRIVATE_API_URL } from "$env/static/private";
export async function load({params, cookies}){
    const base_api = PRIVATE_API_URL
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