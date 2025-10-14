<script>
    import { joinEvent } from "./joinEvent";
    let { event } = $props()
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

    const base_api = import.meta.env.VITE_API_URL
    
</script>

<div class="bg-white rounded-2xl shadow-lg overflow-hidden flex flex-col lg:flex-row items-center gap-6 p-6 hover:shadow-2xl transition duration-300">
    <!-- Image -->
    <div class="flex-shrink-0">
        <img src={img} alt={event.title} class="w-48 h-48 object-cover rounded-xl shadow-md">
    </div>

    <!-- Info -->
    <div class="flex-1 flex flex-col justify-between gap-4">
        <div>
            <h2 class="text-3xl font-bold text-gray-900">{event.title}</h2>
            <p class="text-gray-500 mt-1">{event.start_date} • {event.location}</p>
        </div>

        <div class="flex items-center gap-3 text-blue-500">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 12l4.243-4.243M6 12h12"/>
            </svg>
            <p class="text-lg">{event.start_datetime} - {event.end_datetime}</p>
        </div>
    </div>

    <!-- Actions -->
    <div class="flex flex-col gap-3 lg:mt-0 mt-4">
        {#if event.now_capacity < event.max_capacity}
            <button class="bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg py-3 px-6 transition duration-200" onclick={() => joinEvent(event.id)}>
                Join us
            </button>
        {:else}
            <button class="bg-gray-300 text-gray-600 font-semibold rounded-lg py-3 px-6 cursor-not-allowed">
                Full
            </button>
        {/if}

        <button class="border-2 border-gray-300 text-gray-700 font-semibold py-3 px-6 rounded-lg hover:bg-gray-100 transition duration-200" onclick={openModal}>
            More Info
        </button>
    </div>
</div>

{#if isModalShow}
<div class="fixed inset-0 z-50 flex items-center justify-center">
    <!-- Background overlay -->
    <div class="absolute inset-0 bg-black/50"></div>

    <!-- Modal content -->
    <section class="relative bg-white rounded-2xl shadow-2xl w-[40%] max-lg:w-[90%] p-6 overflow-y-auto max-h-[90vh] z-10 space-y-6">
        
        <!-- Header -->
        <div class="flex justify-between items-center">
            <p class="text-2xl font-bold text-blue-800">{event.title}</p>
            <span class="bg-blue-500 text-white px-4 py-1 rounded-2xl text-sm font-medium">{event.category_name.name}</span>
        </div>

        <!-- Created by -->
        <div class="flex items-center space-x-2 text-blue-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            <p>{event.created_by.username}</p>
        </div>

        <!-- Event Image -->
        <img src={`${base_api}${event.img_url}`} alt={event.title} class="w-full rounded-lg shadow-md object-cover">

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
        <div class="grid grid-cols-3 gap-4 text-center">
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

        <!-- Action buttons -->
        <div class="flex justify-end gap-4 mt-6 max-sm:flex-col">
            <button class="px-5 py-2 bg-blue-500 text-white rounded-lg font-bold shadow-md hover:bg-blue-600 duration-200" onclick={closeModal}>
                Close
            </button>

            {#if event.now_capacity < event.max_capacity}
                <button class="px-5 py-2 bg-blue-500 text-white rounded-lg font-bold shadow-md hover:bg-blue-600 duration-200" onclick={() => joinEvent(event.id)}>
                    Join us
                </button>
            {:else}
                <button class="px-5 py-2 bg-gray-300 text-gray-600 rounded-lg font-bold shadow-sm cursor-not-allowed">
                    Full
                </button>
            {/if}
        </div>

    </section>
</div>
{/if}


<style>
    @keyframes fadeIn { 0% { opacity:0; transform:translateY(-10px);} 100% {opacity:1; transform:translateY(0);} }
    .animate-fadeIn { animation: fadeIn 0.3s ease-out; }
</style>
