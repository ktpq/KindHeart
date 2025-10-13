//@ts-ignore

export async function load({fetch , params}){
    const base_api = import.meta.env.VITE_API_URL
    const response = await fetch(`${base_api}/api/event/${params.id}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "include"
    })

    const data = await response.json()
    return {
        event: data
    }
}