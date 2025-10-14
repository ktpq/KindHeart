<script>
    import AllUser from "./AllUser.svelte";
    import AllEvent from "./AllEvent.svelte";
    import Cookies from 'js-cookie';
    import axios from "axios";
    export let data;

    let isUserShow = true;
    let isEventShow = false;
    let isSendNotiShow = false;

    const openNotiModal = () => {
        isSendNotiShow = true;
        document.body.style.overflow = "hidden";
    }

    const closeNotiModal = () => {
        isSendNotiShow = false;
        document.body.style.overflow = "";
    }

    const showUserPage = () =>{
        isUserShow = true;
        isEventShow = false;
    }

    const showEventPage = () => {
        isUserShow = false;
        isEventShow = true;
    }

    let allEvent = data.allEvent;
    let allUser = data.allUser;
    let userCount = data.userCount;
    let eventCount = data.eventCount;
    let thisMonthCount = data.thismonth_count;

    let notiTile = "";
    let notiDescription = "";

    const base_api = import.meta.env.VITE_API_URL;
    const token = Cookies.get('authToken');

    const sendNotification = async () => {
        if (!notiTile || !notiDescription){
            alert("โปรดใส่รายละเอียดแจ้งเตือนให้ครบ");
            return;
        }
        try {
            await axios.post(`${base_api}/api/notification/`, {title: notiTile, description: notiDescription}, {
                headers: { Authorization: `Token ${token}`}
            });
            alert("ส่ง notification สำเร็จแล้ว");
            window.location.reload();
        } catch (error){
            console.log(error.message);
        }
    }
</script>

<div class="mb-6">
    <a class="flex items-center space-x-3 cursor-pointer hover:text-blue-700 duration-200" href="/">
        <img src="/admin/logout.png" alt="" width="40">
        <p class="text-blue-600 font-semibold text-2xl"> Go back </p>
    </a>
</div>

<div class="mt-8 flex justify-between items-center max-md:flex-col max-md:space-y-3">
    <h1 class="text-5xl font-bold max-md:text-3xl text-blue-700">Admin Dashboard</h1>
    <button class="cursor-pointer text-white bg-blue-600 px-5 py-2 flex items-center space-x-3 hover:bg-blue-700 duration-200 rounded-lg shadow-md" onclick={openNotiModal}>
        <img src="/admin/white-bell.png" alt="" width="25">
        <p> Send Announcement</p>
    </button>
</div>

<!-- Stats -->
<div class="grid grid-cols-3 mt-12 gap-4 max-md:grid-cols-1">
    <div class="shadow-lg rounded-lg p-7 hover:-translate-y-1 duration-200 bg-blue-50">
        <div class="flex justify-between items-center">
            <h2 class="text-xl font-bold text-blue-700">Total Users in system</h2>
            <img src="/admin/people-red.png" alt="" width="40">
        </div>
        <h3 class="text-4xl font-bold mt-10 text-blue-800">{userCount}</h3>
    </div>

    <div class="shadow-lg rounded-lg p-7 hover:-translate-y-1 duration-200 bg-blue-100">
        <div class="flex justify-between items-center">
            <h2 class="text-xl font-bold text-blue-700">Total Events</h2>
            <img src="/admin/calendar-blue.png" alt="" width="40">
        </div>
        <h3 class="text-4xl font-bold mt-10 text-blue-800">{eventCount}</h3>
    </div>

    <div class="shadow-lg rounded-lg p-7 hover:-translate-y-1 duration-200 bg-blue-200">
        <div class="flex justify-between items-center">
            <h2 class="text-xl font-bold text-red-500">New Events this month</h2>
            <img src="/admin/graph-yellow.png" alt="" width="40">
        </div>
        <h3 class="text-4xl font-bold mt-10 text-red-500">{thisMonthCount}</h3>
    </div>
</div>

<!-- Manage system -->
<div class="shadow-lg mt-12 p-7 bg-blue-50 rounded-xl">
    <h3 class="text-4xl font-semibold text-blue-700">Manage System</h3>
    <p class="text-xl font-semibold mt-3 text-blue-400">Manage users and events</p>

    <div class="grid grid-cols-2 mt-6 py-2 px-3 gap-4 rounded-2xl shadow-sm bg-white">
        <button class={`py-2 font-bold rounded-xl cursor-pointer ${isUserShow ? "bg-blue-100 text-blue-800": "text-blue-600"}`} onclick={showUserPage}> Users </button>
        <button class={`py-2 font-bold rounded-xl cursor-pointer ${isEventShow ? "bg-blue-100 text-blue-800": "text-blue-600"}`} onclick={showEventPage}> Events </button>
    </div>

    <div class="mt-6 h-[250px] overflow-auto px-3 max-md:px-0">
        {#if isUserShow}
            <AllUser allUser={allUser}/>
        {/if}
        {#if isEventShow}
            <AllEvent allEvent={allEvent}/>
        {/if}
    </div>
</div>

<!-- Notification Modal -->
{#if isSendNotiShow}
<div class="fixed inset-0 bg-black/50 z-40"></div>
<div class="fixed inset-0 flex items-center justify-center z-50">
    <section class="w-[30%] p-7 font-semibold rounded-2xl shadow-md overflow-y-auto bg-white max-lg:w-[90%] max-sm:mt-30">
        <div class="flex items-center space-x-3">
            <img src="/admin/noti-orange.png" alt="" width="30">
            <p class="text-xl font-semibold text-blue-700">Send a notification to all users</p>
        </div>
        <p class="text-md text-gray-500 mt-2">Enter notification title and description</p>

        <p class="mt-5 text-xl text-blue-700">Title</p>
        <input type="text" class="border w-full mt-3 py-2 text-lg focus:outline-none px-5 border-gray-300 rounded-xl" placeholder="Enter notification title" bind:value={notiTile}>

        <p class="mt-5 text-xl text-blue-700">Description</p>
        <textarea class="border w-full mt-3 py-2 text-lg focus:outline-none px-5 border-gray-300 rounded-xl" placeholder="Enter notification description" bind:value={notiDescription}></textarea>

        <div class="flex justify-end items-center space-x-4 mt-4">
            <button class="px-6 py-2 bg-gray-200 rounded-lg hover:bg-gray-300 duration-200 font-bold" onclick={closeNotiModal}>Cancel</button>
            <button class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 duration-200 font-bold" onclick={sendNotification}>Send</button>
        </div>
    </section>
</div>
{/if}
