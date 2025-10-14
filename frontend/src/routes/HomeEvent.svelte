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
<div class="fixed inset-0 z-50 flex items-center justify-center px-4">
    <div class="absolute inset-0 bg-black/50 backdrop-blur-sm transition-opacity" onclick={closeModal}></div>

    <div class="relative bg-white w-full max-w-3xl rounded-3xl shadow-2xl overflow-y-auto max-h-[90vh] p-8 animate-fadeIn">
        <div class="flex justify-between items-center flex-wrap gap-4">
            <h2 class="text-4xl font-bold text-gray-900">{event.title}</h2>
            <span class="bg-blue-500 text-white px-4 py-1 rounded-full text-sm font-medium">{event.category_name.name}</span>
        </div>

        <div class="flex items-center gap-2 mt-3 text-gray-500">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A9 9 0 1118.879 6.196 9 9 0 015.121 17.804z"/>
            </svg>
            <span>{event.created_by.username}</span>
        </div>

        <img src={`${base_api}${event.img_url}`} alt="activity" class="w-full mt-6 rounded-xl shadow-md object-cover">

        <div class="mt-6">
            <h3 class="text-2xl font-bold text-gray-800">Description</h3>
            <p class="mt-2 text-gray-600 leading-relaxed">{event.description}</p>
        </div>

        <div class="mt-6">
            <h3 class="text-2xl font-bold text-gray-800">Location</h3>
            <p class="mt-2 text-gray-600">{event.location}</p>
        </div>

        <div class="grid grid-cols-2 gap-6 mt-6 max-sm:grid-cols-1">
            <div class="flex items-center gap-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3"/>
                </svg>
                <div>
                    <p class="text-gray-700 font-medium">Start: {event.start_datetime}</p>
                    <p class="text-gray-700 font-medium">End: {event.end_datetime}</p>
                </div>
            </div>
            <div class="flex items-center gap-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M19 3v4M5 21h14a2 2 0 002-2V7H3v12a2 2 0 002 2z"/>
                </svg>
                <p class="text-3xl font-bold text-gray-900">{event.max_capacity}</p>
            </div>
        </div>

        <div class="flex gap-4 mt-8 max-sm:flex-col">
            <button class="flex-1 py-3 border-2 border-gray-300 text-gray-700 font-semibold rounded-lg hover:bg-gray-100 transition duration-200" onclick={closeModal}>
                Cancel
            </button>

            {#if event.now_capacity < event.max_capacity}
                <button class="flex-1 py-3 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 transition duration-200" onclick={() => joinEvent(event.id)}>
                    Join us
                </button>
            {:else}
                <button class="flex-1 py-3 bg-gray-300 text-gray-600 font-semibold rounded-lg cursor-not-allowed">
                    Full
                </button>
            {/if}
        </div>
    </div>
</div>
{/if}

<style>
    @keyframes fadeIn { 0% { opacity:0; transform:translateY(-10px);} 100% {opacity:1; transform:translateY(0);} }
    .animate-fadeIn { animation: fadeIn 0.3s ease-out; }
</style>
