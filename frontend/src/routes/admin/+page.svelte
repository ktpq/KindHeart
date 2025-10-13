<script>
    import AllUser from "./AllUser.svelte";
    import AllEvent from "./AllEvent.svelte";
    export let data
    let isUserShow = true
    let isEventShow = false

    let isSendNotiShow = false

    const openNotiModal = () => {
        isSendNotiShow = true;
        document.body.style.overflow = "hidden"
    }

    const closeNotiModal = () => {
        isSendNotiShow = false;
        document.body.style.overflow = ""
    }

    const showUserPage = () =>{
        isUserShow = true
        isEventShow = false
    }

    const showEventPage = () => {
        isUserShow = false
        isEventShow = true
    }

    let allEvent = data.allEvent

</script>

<div>
    <a class="flex items-center space-x-3 cursor-pointer" href="/">
        <img src="/admin/logout.png" alt="" width="40">
        <p class="text-red-500 font-semibold text-2xl"> Go back </p>
    </a>
</div>

<div class="mt-10 flex justify-between items-center max-md:flex-col max-md:space-y-3">
    <h1 class="text-5xl font-bold max-md:text-3xl"> Admin Dashboard </h1>
    <button class="cursor-pointer text-white bg-[#FFB97C] px-5 py-2 flex items-center space-x-3 hover:bg-[#d38a4a] duration-200 rounded-lg shadow-md" onclick={openNotiModal}>
        <img src="/admin/white-bell.png" alt="" width="25">
        <p> Send Announcement</p>
    </button>
</div>

<div class="grid grid-cols-3 mt-12 gap-4 max-md:grid-cols-1">

    <div class="shadow-lg rounded-lg p-7 hover:-translate-y-1 duration-200 bg-[#D3E4CD]">
        <div class="flex justify-between items-center">
            <h2 class="text-xl font-bold"> Total Users in system </h2>
            <img src="/admin/people-red.png" alt="" width="40">
        </div>
        <h3 class="text-4xl font-bold mt-10 text-[#FE4343]"> 1247</h3>
    </div>

    <div class="shadow-lg rounded-lg p-7 hover:-translate-y-1 duration-200 bg-[#ADC2A9]">
        <div class="flex justify-between items-center">
            <h2 class="text-xl font-bold"> Total Events </h2>
            <img src="/admin/calendar-blue.png" alt="" width="40">
        </div>
        <h3 class="text-4xl font-bold mt-10 text-[#4359FE]"> 1247</h3>
    </div>

    <div class="shadow-lg rounded-lg p-7 hover:-translate-y-1 duration-200 bg-[#99A799]">
        <div class="flex justify-between items-center">
            <h2 class="text-xl font-bold"> New Events this month </h2>
            <img src="/admin/graph-yellow.png" alt="" width="40">
        </div>
        <h3 class="text-4xl font-bold mt-10 text-[#FEF843]"> 12 </h3>
    </div>
    
</div>

<div class="shadow-lg mt-12 p-7 bg-[#D3E4CD]">
    <h3 class="text-4xl font-semibold"> Manage system </h3>
    <p class="text-xl font-semibold mt-5 text-[#ADC2A9]"> Manage users and events  </p>


    <!-- Manage section -->
    <div class="bg-[#f1f2f4] grid grid-cols-2 mt-8 py-2 px-5 gap-4 rounded-2xl shadow-sm">
        <button class={`py-2 font-bold rounded-xl cursor-pointer ${isUserShow ? "bg-white": null}`} onclick={showUserPage}> Users </button>
        <button class={`py-2 font-bold rounded-xl cursor-pointer ${isEventShow ? "bg-white": null}`} onclick={showEventPage}> Events </button>
    </div>


    
    <div class="mt-8 h-[250px] overflow-auto px-3 max-md:px-0">
        <!-- users or events -->
        {#if isUserShow}
        <AllUser/>
        {/if}
        {#if isEventShow}
        <AllEvent allEvent = {allEvent}/>
        {/if}

    </div>
</div>

{#if isSendNotiShow}
<div class="fixed inset-0 bg-black/50 z-40"></div>
<div class="fixed inset-0 flex items-center justify-center z-50">
    <section class="w-[30%] p-7 font-semibold rounded-2xl shadow-md overflow-y-auto bg-white max-lg:w-[90%] max-sm:mt-30">
        <div class="flex items-center space-x-3">
            <img src="/admin/noti-orange.png" alt="" width="30">
            <p class="text-xl font-semibold"> Send a notification to all users </p>
        </div>
        <p class="text-md text-gray-500 mt-3"> Enter notification Title and Description </p>

        <p class="mt-5 text-xl"> Title </p>
        <input type="text" class="border w-full mt-3 py-2 text-lg focus:outline-none px-5 border-gray-300 rounded-xl" placeholder="Enter notification title">

        <p class="mt-5 text-xl"> Description </p>
        <textarea name="" id="" class="border w-full mt-3 py-2 text-lg focus:outline-none px-5 border-gray-300 rounded-xl" placeholder="Enter notification description"></textarea>

        <div class="flex justify-end items-center space-x-4 mt-4">
            <button class="btn-white" onclick={closeNotiModal}>Cancel</button>
            <button class="btn-orange">Send</button>
        </div>
    </section>
</div>
{/if}



