import { writable } from "svelte/store";
import Cookies from 'js-cookie';
import axios from "axios";

export interface UserType{
    id: number
    username: string
    email: string
    is_staff: boolean
    status: string
}

export const user = writable<UserType | null>(null)

export const loadUser = async () => {
    const token = Cookies.get('authToken')
    if (!token){
        user.set(null)
        return
    }

    try{
        const base_api = import.meta.env.VITE_API_URL
        const response = await axios.get(`${base_api}/api/auth/myprofile`,{
            headers: { Authorization: `Token ${token}`}
        })

        user.set(response.data)
        console.log("from store", response.data)
    } catch (error){
        console.log("failed to fetch user", error)
        user.set(null)
    }
}