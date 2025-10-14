<script>
    import Swal from "sweetalert2";
    import { joinEvent } from "./joinEvent";
    let { event } = $props()
    import { formatDate, formatDateTime, formatTimeUTC } from "./format";
    let isModalShow = $state(false)

    const img = import.meta.env.VITE_API_URL + event.img_url
    const openModal = () => {
        isModalShow = true
        document.body.style.overflow = "hidden"
    }

    const closeModal = () =>{
        isModalShow = false
        document.body.style.overflow = "" 
    }

    

    
</script>

<div class="border-t-4 border-[#D3E4CD] p-5 flex justify-between items-center my-4 max-lg:flex-col">
    <!-- box ซ้าย -->
    <div class="py-2 flex items-center justify-between space-x-8 max-lg:flex-col max-lg:space-x-0 max-lg:space-y-4">
        
        <p class="text-2xl font-semibold">{event.start_date} </p>
        
        <img src={img} alt="" class="min-w-[100px]" width="150">
        <div>
            <p class="text-3xl font-bold font-main"> {event.title} </p>
            <div class="flex items-center space-x-4 mt-3 ">
                <img src="/home/location.png" alt="" width="30">
                <p class="text-xl font-semibold text-[#ADC2A9]"> {event.location} • {event.start_datetime} - {event.end_datetime} </p>
            </div>
        </div>
    </div>
    <!-- box ขวา -->
    <div class="flex flex-col justify-center space-y-3 max-lg:mt-5">
        {#if event.now_capacity < event.max_capacity}
        <button class="bg-[#FFB97C] px-5 text-xl py-3 text-white rounded-lg font-bold hover:bg-[#ee9e59] duration-200 cursor-pointer" onclick={() => {joinEvent(event.id)}}> Join us</button>
        {:else}
        <button class="bg-[#FFB97C] px-5 text-xl py-3 text-white rounded-lg font-bold hover:bg-[#ee9e59] duration-200 cursor-pointer"> full </button>
        {/if}
        <button class="px-6 text-xl py-3 border-3 border-[#ADC2A9] text-[#9ba69b] rounded-lg font-bold cursor-pointer hover:bg-[#ebdfd3] duration-200" onclick={openModal}> More Info </button>
    </div>
    
</div>

<!-- Event modal -->
{#if isModalShow}
<div class="fixed inset-0 bg-black/50 z-40"></div>
<div class="fixed inset-0 flex items-center justify-center z-50">
    <section class="w-[40%] p-10 font-semibold rounded-2xl shadow-md h-[800px] overflow-y-auto bg-white max-lg:w-[90%] max-sm:mt-30">
        <div class="flex justify-between items-center max-sm:flex-col max-sm:space-y-3">
            <p class="text-3xl font-bold"> {event.title} </p>
            <p class="bg-[#1AD048] text-white px-5 py-1 rounded-2xl"> {event.category_name.name} </p>
        </div>
        <div class="mt-4 flex items-center space-x-2 max-sm:justify-center">
            <img src="/home/person.png" alt="" width="25">
            <p class="text-[#8E8B8B]"> {event.created_by.username} </p>
        </div>
        <img src="/home/activity.png" alt="" class="w-full mt-4">

        <div class="mt-6">
            <p class="text-3xl font-bold"> Description </p>
            <p class="mt-3 text-[#8E8B8B]"> {event.description}</p>
        </div>

        <div class="mt-6">
            <p class="text-3xl font-bold"> Location </p>
            <p class="mt-3 text-[#8E8B8B]"> {event.location} </p>
        </div>

        <div class="grid grid-cols-2 gap-3 mt-5 max-sm:flex max-sm:flex-col">
            <div class="items-center space-x-4 flex space-x-4">
                <img src="/home/time.png" alt="" width="50">
                <div>
                    <p class="text-lg"> start :{event.start_datetime}</p>
                    <p class="text-lg"> end : {event.end_datetime} </p>
                </div>
            </div>
            <div class="flex items-center space-x-4">
                <img src="/home/people.png" alt="" width="50">
                <p class="text-3xl"> {event.max_capacity} </p>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-5 max-sm:flex max-sm:flex-col max-sm:gap-0">
            <button class="max-sm:w-full max-sm:my-2 shadow-md my-5 py-3 border-2 text-[#8E8B8B] font-bold text-xl hover:bg-[#f1f1f1] duration-200 rounded-lg" onclick={closeModal}>
            Cancel
            </button>
            
            {#if event.now_capacity < event.max_capacity}
            <button class="max-sm:w-full max-sm:my-2 shadow-md my-5 py-3 text-white bg-[#FFB97C] font-bold text-xl hover:bg-[#d89458] duration-200 rounded-lg" onclick={() => {joinEvent(event.id)}}>
            Join us 
            </button>
            {:else}
            <button class="max-sm:w-full max-sm:my-2 shadow-md my-5 py-3 text-white bg-[#FFB97C] font-bold text-xl hover:bg-[#d89458] duration-200 rounded-lg">
            full
            </button>
            {/if}
            
        </div>
    </section>
</div>
{/if}


