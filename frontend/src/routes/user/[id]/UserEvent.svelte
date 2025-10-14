<script>
    let { event } = $props();
    let isModalShow = $state(false)

    const openModal = () => {
        isModalShow = true;
        document.body.style.overflow = "hidden";
    }

    const closeModal = () => {
        isModalShow = false;
        document.body.style.overflow = "";
    }

    const base_api = import.meta.env.VITE_API_URL;
</script>

<!-- Event Card -->
<div class="bg-white shadow-lg rounded-xl p-5 flex justify-between items-center my-4 max-lg:flex-col max-lg:space-y-4 transition hover:shadow-2xl hover:-translate-y-1">

    <!-- Left -->
    <div class="flex items-center space-x-6 max-lg:flex-col max-lg:space-x-0 max-lg:space-y-4">
        <img src={`${base_api}${event.img_url}`} alt="" class="w-32 h-32 rounded-lg object-cover shadow-md">

        <div class="space-y-2">
            <div class="flex items-center space-x-4">
                <p class="text-2xl font-bold text-blue-800">{event.title}</p>
                <p class="px-4 py-1 rounded-full text-sm font-semibold bg-blue-100 text-blue-700">
                    {event.category_name.name}
                </p>
            </div>
            <div class="flex items-center space-x-3 text-blue-600">
                <!-- Location SVG -->
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 12l4.243-4.243M6 12h18" />
                </svg>
                <p class="text-lg">{event.location} • {event.start_datetime} - {event.end_datetime}</p>
            </div>
        </div>
    </div>

    <!-- Right -->
    <div class="flex flex-col justify-center space-y-3 max-lg:flex-row max-lg:space-x-3 max-lg:space-y-0">
        <button class="bg-blue-500 text-white px-5 py-3 rounded-lg font-bold hover:bg-blue-600 shadow-md duration-200 cursor-pointer" onclick={openModal}>
            More Info
        </button>
    </div>
</div>

<!-- Event Modal -->
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
            <button class="px-5 py-2 bg-blue-500 text-white rounded-lg font-bold shadow-md hover:bg-blue-600 duration-200" onclick={closeModal}>
                Close
            </button>
        </div>

    </section>
</div>
{/if}
