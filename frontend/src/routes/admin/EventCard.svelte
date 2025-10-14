<script>
    let { event } = $props()
    import Swal from "sweetalert2";
    import { goto, invalidateAll } from "$app/navigation";
    import Cookies from 'js-cookie'
    import axios from "axios";
    let isModalShow = $state(false)
    const base_api = import.meta.env.VITE_API_URL
    const token = Cookies.get('authToken')
    const deleteEvent = (event_id) => {
        Swal.fire({
        title: "Are you sure?",
        text: "คุณต้องการลบกิจกรรมนี้ใช่หรือไม่",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "ยืนยัน",
        cancelButtonText: "ยกเลิก",
        
        }).then(async (result) => {
        if (result.isConfirmed) {

            // ยิง api
            const response = await axios.delete(`${base_api}/api/event/${event_id}/` ,{
                headers: {
                    Authorization: `Token ${token}`
                }
            })

            console.log(response.data)
            // window.location.href = "/admin"
            Swal.fire({
                title: "ลบกิจกรรมสำเร็จ!",
                icon: "success"
            }).then(() => {
                window.location.href = "/admin"
            })
            
        }
        });
    }
</script>

<div class="bg-white flex justify-between items-center p-5 shadow-md rounded-xl hover:-translate-y-1 duration-200 my-3 max-md:flex-col max-md:space-y-3">
    <div>
        <h2 class="text-xl font-bold"> {event.title} </h2>
        <h3 class="text-lg font-semibold mt-2 text-[#ADC2A9]"> {event.start_datetime} </h3>
    </div>
    <div class="flex items-center space-x-3">
        <button class="px-5 py-2 text-xl font-semibold  border-gray-200 hover:bg-[#d3d2d2] duration-200 rounded-xl shadow-md cursor-pointer" onclick={() =>{isModalShow = !isModalShow}}> View info </button>
        <button class="px-5 py-2 text-white text-xl font-semibold bg-[#FE9A9C] hover:bg-[#ce6668] duration-200 rounded-xl shadow-md cursor-pointer" onclick={() => {deleteEvent(event.id)}}> Delete </button>
    </div>
</div>

{#if isModalShow}
<div class="fixed inset-0 z-50 flex items-center justify-center px-4">
    <!-- Background overlay -->
    <div class="absolute inset-0 bg-black/50 backdrop-blur-sm transition-opacity" onclick={closeModal}></div>

    <!-- Modal content -->
    <section class="relative bg-white w-full max-w-3xl rounded-2xl shadow-2xl overflow-y-auto max-h-[90vh] p-8 space-y-6 z-10">

        <!-- Header -->
        <div class="flex justify-between items-center flex-wrap gap-4">
            <h2 class="text-3xl font-bold text-blue-800">{event.title}</h2>
            <span class="bg-blue-500 text-white px-4 py-1 rounded-full text-sm font-medium">{event.category_name.name}</span>
        </div>

        <!-- Created by -->
        <div class="flex items-center gap-2 text-blue-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/>
            </svg>
            <span>{event.created_by.username}</span>
        </div>

        <!-- Event Image -->
        <img src={`${base_api}${event.img_url}`} alt={event.title} class="w-full rounded-xl shadow-md object-cover mt-4">

        <!-- Description -->
        <div>
            <p class="text-blue-800 font-semibold mb-1">Description</p>
            <p class="text-gray-600">{event.description}</p>
        </div>

        <!-- Location -->
        <div>
            <p class="text-blue-800 font-semibold mb-1">Location</p>
            <p class="text-gray-600">{event.location}</p>
        </div>

        <!-- Event Details -->
        <div class="grid grid-cols-3 gap-4 text-center mt-5 max-sm:grid-cols-1">
            <div class="bg-blue-50 p-3 rounded-lg shadow-sm">
                <p class="text-sm text-gray-500">Start</p>
                <p class="font-semibold text-blue-700">{event.start_datetime}</p>
            </div>
            <div class="bg-blue-50 p-3 rounded-lg shadow-sm">
                <p class="text-sm text-gray-500">End</p>
                <p class="font-semibold text-blue-700">{event.end_datetime}</p>
            </div>
            <div class="bg-blue-50 p-3 rounded-lg shadow-sm">
                <p class="text-sm text-gray-500">Max Capacity</p>
                <p class="font-semibold text-blue-700">{event.max_capacity}</p>
            </div>
        </div>

        <!-- Action Button -->
        <div class="flex justify-end mt-6">
            <button class="px-5 py-2 bg-blue-500 text-white rounded-lg font-bold shadow-md hover:bg-blue-600 duration-200" onclick={() => {isModalShow = false}}>
                Close
            </button>
        </div>

    </section>
</div>
{/if}
