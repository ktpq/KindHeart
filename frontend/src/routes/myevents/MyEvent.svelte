<script lang="ts">
    import { onMount } from "svelte";
    import Cookies from "js-cookie";
    import axios from "axios";
    import Swal from "sweetalert2";

    let { event } = $props();
    const base_api = import.meta.env.VITE_API_URL;

    let isModalShow = $state(false);
    let inputCode = "";
    let users = [];

    const openModal = () => {
        isModalShow = true;
        document.body.style.overflow = "hidden";
    };

    const closeModal = () => {
        isModalShow = false;
        document.body.style.overflow = "";
    };

    const getEventStatus = (end_time: string) => {
        const now = new Date();
        const end = new Date(end_time);
        if (now > end) {
            return { text: "Success", bg: "#BCF5C5", color: "#00E043" }; // เขียว
        } else {
            return { text: "On-going", bg: "#FFD966", color: "#E08900" }; // ส้ม
        }
    };

    let status = getEventStatus(event.end_time);

    onMount(() => {
        const fetchAllUser = async () => {
            try {
                const token = Cookies.get('authToken');
                const response = await axios.get(`${base_api}/api/participation/event/${event.id}/`, {
                    headers: { Authorization: `Token ${token}` }
                });
                users = response.data;
            } catch (error) {
                console.error(error);
            }
        };
        fetchAllUser();
    });

    const checkParticipation = async () => {
        try {
            const token = Cookies.get('authToken');
            await axios.put(`${base_api}/api/participation/event/${event.id}/`, { ticket_code: inputCode }, {
                headers: { Authorization: `Token ${token}` }
            });

            await Swal.fire({
                icon: 'success',
                title: 'Check-in Success!',
                text: 'เช็คชื่อเรียบร้อย',
                confirmButtonColor: '#EF4444', // ปุ่ม OK สีแดง
                confirmButtonText: 'OK'
            });

            window.location.reload();
        } catch (error) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'ไม่พบผู้ใช้ในกิจกรรมของคุณ',
                confirmButtonColor: '#EF4444',
                confirmButtonText: 'OK'
            });
        }
    };
</script>

<!-- Event Card -->
<div class="bg-white shadow-lg rounded-xl p-5 flex justify-between items-center my-4 max-lg:flex-col max-lg:space-y-4 hover:shadow-2xl transition hover:-translate-y-1">
    <!-- Left -->
    <div class="flex items-center space-x-6 max-lg:flex-col max-lg:space-x-0 max-lg:space-y-4">
        <img src={`${base_api}/${event.img_url}`} alt="" class="w-32 h-32 rounded-lg object-cover shadow-md">
        <div class="space-y-2">
            <div class="flex items-center space-x-3 max-sm:flex-col max-sm:space-y-2">
                <p class="text-2xl font-bold text-blue-600">{event.title}</p>
                <p class="px-4 py-1 rounded-full text-sm font-semibold" style="background-color: {status.bg}; color: {status.color}">
                    {status.text}
                </p>
            </div>
            <div class="flex items-center space-x-3 text-blue-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 12l4.243-4.243M6 12h18" />
                </svg>
                <p class="text-lg">{event.location} • {event.start_datetime} - {event.end_datetime}</p>
            </div>
        </div>
    </div>

    <!-- Right -->
    <div class="flex flex-col justify-center space-y-3 max-lg:flex-row max-lg:space-x-3 max-lg:space-y-0">
        <button class="bg-blue-600 text-white px-5 py-3 rounded-lg font-bold hover:bg-blue-700 shadow-md duration-200 cursor-pointer" onclick={openModal}>
            Participants
        </button>
        <a class="border-2 border-blue-400 text-blue-600 px-5 py-3 rounded-lg font-bold hover:bg-blue-50 shadow-md duration-200 cursor-pointer text-center" href={`/edit/${event.id}`}>
            Edit
        </a>
    </div>
</div>

<!-- Participants Modal -->
{#if isModalShow}
<div class="fixed inset-0 z-50 flex items-center justify-center">
    <!-- Background -->
    <div class="absolute inset-0 bg-black/80"></div>

    <!-- Modal Content -->
    <section class="relative bg-white rounded-2xl shadow-2xl w-[50%] max-lg:w-[90%] p-6 overflow-y-auto max-h-[80vh] z-10 space-y-6">
        <div class="flex justify-between items-center mb-4">
            <h1 class="text-3xl font-bold text-blue-600">Participants</h1>
            <button class="text-gray-300 font-bold text-2xl" onclick={closeModal}>×</button>
        </div>

        <!-- Check Ticket -->
        <div class="flex gap-3 max-sm:flex-col">
            <input type="text" placeholder="Enter ticket code" class="flex-1 border-2 border-blue-600 rounded-2xl py-2 px-4 shadow-md focus:outline-none" bind:value={inputCode}>
            <button class="bg-red-500 text-white py-2 px-6 rounded-lg font-bold shadow-md hover:bg-red-600 transition" onclick={checkParticipation}>
                Check
            </button>
        </div>

        <!-- Participants Table -->
        <div class="overflow-y-auto max-h-[300px]">
            <table class="w-full text-left text-sm md:text-base table-fixed">
                <thead class="bg-gray-100">
                    <tr>
                        <th class="px-4 py-2 w-1/12">ID</th>
                        <th class="px-4 py-2 w-3/12">Username</th>
                        <th class="px-4 py-2 w-5/12">Ticket Code</th>
                        <th class="px-4 py-2 w-3/12">Status</th>
                    </tr>
                </thead>
                <tbody>
                    {#each users as user}
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-2">{user.user.id}</td>
                        <td class="px-4 py-2">{user.user.username}</td>
                        <td class="px-4 py-2">{user.ticket_code}</td>
                        <td class="px-4 py-2 {user.attended ? 'text-green-500' : 'text-red-500'}">
                            {user.attended ? 'Attended' : 'Absent'}
                        </td>
                    </tr>
                    {/each}
                </tbody>
            </table>
        </div>

        <div class="flex justify-end">
            <button class="px-5 py-2 bg-blue-600 text-white rounded-lg font-bold shadow-md hover:bg-blue-700 transition" onclick={closeModal}>
                Close
            </button>
        </div>
    </section>
</div>
{/if}
