// +page.js
import axios from "axios";
import Cookies from "js-cookie";

export async function load() {
    const base_api = import.meta.env.VITE_API_URL;
    const token = Cookies.get("authToken");

    if (!token) return { events: [] };

    try {
        // 1. ดึง profile ของผู้ใช้
        const profileResponse = await axios.get(`${base_api}/api/auth/myprofile/`, {
            headers: { Authorization: `Token ${token}` }
        });

        // 2. ดึง events ของผู้ใช้
        const eventsResponse = await axios.get(`${base_api}/api/event/owner/${profileResponse.data.id}/`, {
            headers: { Authorization: `Token ${token}` }
        });

        return {
            events: eventsResponse.data
        };
    } catch (err) {
        console.error(err);
        return { events: [] };
    }
}
