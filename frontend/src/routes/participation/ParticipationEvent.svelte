<script lang="ts">
    import QRCode from 'qrcode'

    let { event } = $props()
    const base_api = import.meta.env.VITE_API_URL

    let isInfoModalShow = $state(false)
    let isQrModalShow = $state(false)

    const openInfoModal = () => {
        isInfoModalShow = true
        document.body.style.overflow = "hidden"
    }

    const closeInfoModal = () =>{
        isInfoModalShow = false
        document.body.style.overflow = "" 
    }

    const openQrModal = () => {
        isQrModalShow = true
        document.body.style.overflow = "hidden"
    }

    const closeQrModal = () => {
        isQrModalShow = false
        document.body.style.overflow = ""
    }

    const getEventStatus = (end_time: string) => {
        const now = new Date();
        const end = new Date(end_time);
        if (now > end) {
            return { text: "Success", bg: "#D4F5E1", color: "#00A86B" }; // เขียว
        } else {
            return { text: "On-going", bg: "#D0E7FF", color: "#0077CC" }; // ฟ้า
        }
    };

    let qrDataUrl = ''
    async function generateQR(){
        if (event?.ticket_code){
            qrDataUrl = await QRCode.toDataURL(event.ticket_code, {
                width: 200,
                margin: 1,
            });
        }
    }

    generateQR()
    let status = getEventStatus(event.event.end_time);
</script>

<!-- Event Card -->
<div class="bg-white shadow-lg rounded-xl p-5 flex justify-between items-center my-4 max-lg:flex-col max-lg:space-y-4 transition hover:shadow-2xl hover:-translate-y-1">
    <!-- Left -->
    <div class="flex items-center space-x-6 max-lg:flex-col max-lg:space-x-0 max-lg:space-y-4">
        <img src={`${base_api}${event.event.img_url}`} alt="" class="w-32 h-32 rounded-lg object-cover shadow-md">

        <div class="space-y-2">
            <div class="flex items-center space-x-4">
                <p class="text-2xl font-bold text-blue-800">{event.event.title}</p>
                <p class="px-4 py-1 rounded-full text-sm font-semibold" style="background-color: {status.bg}; color: {status.color}">
                    {status.text}
                </p>
            </div>
            <div class="flex items-center space-x-3 text-blue-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 12l4.243-4.243M6 12h18" />
                </svg>
                <p class="text-lg">{event.event.location} • {event.event.start_datetime} - {event.event.end_datetime}</p>
            </div>
        </div>
    </div>

    <!-- Right -->
    <div class="flex flex-col justify-center space-y-3 max-lg:flex-row max-lg:space-x-3 max-lg:space-y-0">
        <button class="bg-blue-500 text-white px-5 py-3 rounded-lg font-bold hover:bg-blue-600 shadow-md duration-200 cursor-pointer" onclick={openQrModal}>
            QR Code
        </button>
        <button class="border-2 border-blue-300 text-blue-700 px-5 py-3 rounded-lg font-bold hover:bg-blue-50 shadow-md duration-200 cursor-pointer" onclick={openInfoModal}>
            More Info
        </button>
    </div>
</div>

<!-- Info Modal -->

{#if isInfoModalShow}
<div class="fixed inset-0 z-50 flex items-center justify-center">
    <!-- Background overlay -->
    <div class="absolute inset-0 bg-black/50"></div>

    <!-- Modal content -->
    <section class="relative bg-white rounded-2xl shadow-2xl w-[40%] max-lg:w-[90%] p-6 overflow-y-auto max-h-[90vh] z-10 space-y-6">
        <!-- Header -->
        <div class="flex justify-between items-center">
            <p class="text-2xl font-bold text-blue-800">{event.event.title}</p>
            <p class="bg-blue-500 text-white px-4 py-1 rounded-2xl">{event.event.category_name.name}</p>
        </div>

        <!-- Created by -->
        <div class="flex items-center space-x-2 text-blue-600">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            <p>{event.event.created_by.username}</p>
        </div>

        <!-- Event Image -->
        <img src={`${base_api}${event.event.img_url}`} alt={event.event.title} class="w-full rounded-lg shadow-md object-cover">

        <!-- Description -->
        <div>
            <p class="text-blue-800 font-semibold mb-1">Description</p>
            <p class="text-gray-600">{event.event.description}</p>
        </div>

        <!-- Location -->
        <div>
            <p class="text-blue-800 font-semibold mb-1">Location</p>
            <p class="text-gray-600">{event.event.location}</p>
        </div>

        <!-- Event Details: start/end/max capacity -->
        <div class="grid grid-cols-3 gap-4 text-center">
            <div class="bg-blue-50 p-3 rounded-lg shadow-sm">
                <p class="text-sm text-gray-500">Start</p>
                <p class="font-semibold text-blue-700">{event.event.start_datetime}</p>
            </div>
            <div class="bg-blue-50 p-3 rounded-lg shadow-sm">
                <p class="text-sm text-gray-500">End</p>
                <p class="font-semibold text-blue-700">{event.event.end_datetime}</p>
            </div>
            <div class="bg-blue-50 p-3 rounded-lg shadow-sm">
                <p class="text-sm text-gray-500">Max Capacity</p>
                <p class="font-semibold text-blue-700">{event.event.max_capacity}</p>
            </div>
        </div>

        <!-- Close Button -->
        <div class="flex justify-end">
            <button class="px-5 py-2 bg-blue-500 text-white rounded-lg font-bold shadow-md hover:bg-blue-600 duration-200" onclick={closeInfoModal}>
                Close
            </button>
        </div>
    </section>
</div>
{/if}


<!-- QR Modal -->
{#if isQrModalShow}
<div class="fixed inset-0 z-50 flex items-center justify-center">
    <!-- Background overlay -->
    <div class="absolute inset-0 bg-black/50"></div>

    <!-- Modal content -->
    <section class="relative bg-white rounded-2xl shadow-2xl w-[26%] max-lg:w-[90%] p-5 flex flex-col items-center z-10">
        <h2 class="text-xl font-bold text-white bg-blue-500 w-full text-center py-2 rounded-t-xl mb-4">Ticket Info</h2>
        <img src={qrDataUrl} alt="QR Code" class="shadow-lg rounded-lg mb-3"/>
        <p class="font-bold mb-1">Ticket Code</p>
        <p class="border-2 border-dashed border-blue-200 rounded-lg py-2 px-4 text-center mb-4 w-full">{event.ticket_code}</p>
        <button class="px-5 py-2 bg-blue-500 text-white rounded-lg shadow-md font-bold hover:bg-blue-600 duration-200" onclick={closeQrModal}>
            Close
        </button>
    </section>
</div>
{/if}

