import axios from "axios";

export async function load({ params, cookies }) {
    try{    
        const token = cookies.get('authToken')
    } catch (error){
        console.log(error.message)
    }
}