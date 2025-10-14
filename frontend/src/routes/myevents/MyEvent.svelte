<script lang="ts">
    import { onMount } from "svelte";
    import { formatDate, formatDateTime } from "../format";
    import  Cookies from "js-cookie";
    import axios from "axios";
  import { goto } from "$app/navigation";
    let { event } = $props()
    let isModalShow = $state(false)

    const openModal = () => {
        isModalShow = true
        document.body.style.overflow = "hidden"
    }

    const closeModal = () =>{
        isModalShow = false
        document.body.style.overflow = "" 
    }
    const base_api = import.meta.env.VITE_API_URL

    const getEventStatus = (end_time: string) => {
        const now = new Date();
        const end = new Date(end_time);
        if (now > end) {
            return { text: "Success", bg: "#BCF5C5", color: "#00E043" }; // สีเขียว
        } else {
            return { text: "On-going", bg: "#FFD966", color: "#E08900" }; // สีส้ม
        }
    };

    // สร้างตัวแปร status
    let status = getEventStatus(event.end_time);
    let users = []
    onMount(() => {
        const fetchAllUser = async () => {
            const base_api = import.meta.env.VITE_API_URL
            const token = Cookies.get('authToken')
            const response = await axios.get(`${base_api}/api/participation/event/${event.id}/`, {
                headers: {
                    Authorization: `Token ${token}`
                }
            })
            console.log(response.data)
            users = response.data
        }
        fetchAllUser()
    })

    let inputCode = ""
    const checkParticipation = async () => {
        try {
            const base_api = import.meta.env.VITE_API_URL
            const token = Cookies.get('authToken')
            console.log(event.id)
            const respone = await axios.put(`${base_api}/api/participation/event/${event.id}/`, { "ticket_code": inputCode }, {
                headers: { Authorization: `Token ${token}`}
            })
            alert("เช็คชื่อเรียบร้อย")
            window.location.reload()
            console.log(respone.data)
        } catch (error){
            alert("ไม่พบผู้ใช้ในกิจกรรมของคุณ")
        }
    }
</script>

<div class="border-t-4 border-[#D3E4CD] p-5 flex justify-between items-center my-4 max-lg:flex-col">
    <!-- box ซ้าย -->
     
    <div class="py-2 flex items-center justify-between space-x-8 max-lg:flex-col max-lg:space-x-0 max-lg:space-y-4">
        
        <p class="text-2xl font-semibold">{formatDate(event.start_time)} </p>
        
        <img src={`${base_api}/${event.img_url}`} alt="" class="min-w-[100px]" width="150">
        <div>
            <div class="flex items-center space-x-3 max-sm:flex-col max-sm:space-y-3">
                <p class="text-3xl font-bold font-main"> {event.title}  </p> 
                <p class="text-lg px-4 py-1 rounded-3xl" style="background-color: {status.bg}; color: {status.color}">
                    {status.text}
                </p>
            </div>
            <div class="flex items-center space-x-4 mt-3 ">
                <img src="/home/location.png" alt="" width="30">
                <p class="text-xl font-semibold text-[#ADC2A9]"> {event.location} • {formatDateTime(event.start_time)} - {formatDateTime(event.end_time)} </p>
            </div>
        </div>
    </div>
    <!-- box ขวา -->
    <div class="flex flex-col justify-center space-y-3 max-lg:mt-5">
        <button class="bg-[#FFB97C] px-5 text-xl py-3 text-white rounded-lg font-bold hover:bg-[#ee9e59] duration-200 cursor-pointer" onclick={openModal}> Participants </button>
        <a class="px-6 text-xl py-3 border-3 border-[#ADC2A9] text-[#9ba69b] rounded-lg font-bold cursor-pointer hover:bg-[#ebdfd3] duration-200 text-center" href="/edit/{event.id}"> Edit </a>
    </div>
    
</div>

<!-- Event modal -->
{#if isModalShow}

<div class="fixed inset-0 bg-black/50 z-40"></div>
<div class="fixed inset-0 flex items-center justify-center z-50">
    <section class="w-[50%] max-lg:p-3 p-10 font-semibold rounded-2xl shadow-md h-[500px] bg-white max-lg:w-[90%] max-sm:mt-30">
        <!-- {JSON.stringify(users)} -->
        <div class="flex justify-between items-center px-5">
            <p></p>
            <h1 class="text-center text-4xl text-[#FFB97C] font-semibold"> Participants </h1>
            <button onclick={closeModal} class="cursor-pointer"> close </button>
        </div>
        <div class="p-5 mt-4 grid grid-cols-[10fr_2fr] gap-3 max-sm:flex max-sm:flex-col">
            <input type="text" class="border-2 border-[#FFB97C] rounded-2xl py-2 px-10 shadow-md focus:outline-none" placeholder="Enter ticket code" bind:value={inputCode}>
            <button class="py-2 bg-[#FFB97C] font-bold rounded-lg shadow-md duration-200 hover:bg-[#c7874f] cursor-pointer" onclick={checkParticipation}> Check </button>
        </div>

        <div class="px-5">
            <div class="px-5 mt-4 max-h-[300px] overflow-y-auto max-md:px-0">
            <!-- {JSON.stringify(users)} -->
            <table class="w-full text-sm md:text-xl table-fixed">


                <thead class="bg-gray-100">
                <tr>
                    <th class="px-4 py-2 w-1/12 text-left">ID</th>
                    <th class="px-4 py-2 w-3/12 text-left">Username</th>
                    <th class="px-4 py-2 w-5/12 text-left">Ticket Code</th>
                    <th class="px-4 py-2 w-3/12 text-left">Status</th>
                </tr>
                </thead>
                <tbody>
                {#each users as user}
                <tr class="hover:bg-gray-50">
                    <td class="px-4 py-2">{user.user.id}</td>
                    <td class="px-4 py-2">{user.user.username}</td>
                    <td class="px-4 py-2">{user.ticket_code}</td>
                    {#if user.attended}
                    <td class="px-4 py-2 text-green-500">attended</td>
                    {:else}
                    <td class="px-4 py-2 text-red-500">absent</td>
                    {/if}
                </tr>
                {/each}
                
                <!-- เพิ่ม row ตามต้องการ -->
                </tbody>
            </table>
</div>

        </div>
    </section>
</div>
{/if}


