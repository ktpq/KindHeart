/**
 * @param {{ fetch: typeof fetch, params:any }} param0
 */

export async function load({ params }) {
    const event_id = Number(params.id)
    return {
        id: Number(params.id)
    }
}