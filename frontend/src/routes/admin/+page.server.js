import axios from "axios";
import { PRIVATE_API_URL } from "$env/static/private";

export async function load({cookies}){
    const base_api = PRIVATE_API_URL
    const token = cookies.get('authToken')

    try{
        // get event ทั้งหมด
        const eventResponse = await axios.get(`${base_api}/api/event/`, {
            headers: { Authorization: `Token ${token}`}
        })

        const userResponse = await axios.get(`${base_api}/api/user/`, {
            headers: { Authorization: `Token ${token}`}
        })

        return {
            allEvent: eventResponse.data.events,
            allUser: userResponse.data.users,
            userCount: userResponse.data.user_count,
            eventCount: eventResponse.data.event_count,
            thismonth_count: eventResponse.data.event_thismonth_count
        }
    } catch (error){
        console.log(error.message)
    }

    
}