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
            return { text: "Success", bg: "#BCF5C5", color: "#00E043" }; // สีเขียว
        } else {
            return { text: "On-going", bg: "#FFD966", color: "#E08900" }; // สีส้ม
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
    // สร้างตัวแปร status
    let status = getEventStatus(event.event.end_time);

    
</script>

<div class="border-t-4 border-[#D3E4CD] p-5 flex justify-between items-center my-4 max-lg:flex-col">
    <!-- {JSON.stringify(event.event)} -->
    <!-- box ซ้าย -->
    <div class="py-2 flex items-center justify-between space-x-8 max-lg:flex-col max-lg:space-x-0 max-lg:space-y-4">
        
        <p class="text-2xl font-semibold">{event.event.start_time} </p>
        
        <img src={`${base_api}${event.event.img_url}`} alt="" class="min-w-[100px]" width="150">
        <div>
            <div class="flex items-center space-x-3 max-sm:flex-col max-sm:space-y-3">
                <p class="text-3xl font-bold font-main"> {event.event.title}  </p> 
                <p class="text-lg px-4 py-1 rounded-3xl" style="background-color: {status.bg}; color: {status.color}">
                    {status.text}
                </p>
            </div>
            <div class="flex items-center space-x-4 mt-3 ">
                <img src="/home/location.png" alt="" width="30">
                <p class="text-xl font-semibold text-[#ADC2A9]"> {event.event.location} • {event.event.start_time} - {event.event.end_time} </p>
            </div>
        </div>
    </div>
    <!-- box ขวา -->
    <div class="flex flex-col justify-center space-y-3 max-lg:mt-5">
        <button class="bg-[#FFB97C] px-5 text-xl py-3 text-white rounded-lg font-bold hover:bg-[#ee9e59] duration-200 cursor-pointer" onclick={openQrModal}> Qr Code </button>
        <button class="px-6 text-xl py-3 border-3 border-[#ADC2A9] text-[#9ba69b] rounded-lg font-bold cursor-pointer hover:bg-[#ebdfd3] duration-200" onclick={openInfoModal}> More Info </button>
    </div>
    
</div>

<!-- Info modal -->
{#if isInfoModalShow || isQrModalShow}
<div class="fixed inset-0 bg-black/50 z-40"></div>
{/if}

{#if isInfoModalShow}
<div class="fixed inset-0 flex items-center justify-center z-50">
    <section class="w-[40%] p-10 font-semibold rounded-2xl shadow-md h-[800px] overflow-y-auto bg-white max-lg:w-[90%] max-sm:mt-30">
        <div class="flex justify-between items-center max-sm:flex-col max-sm:space-y-3">
            <p class="text-3xl font-bold"> {event.event.title} </p> 
            <p class="bg-[#1AD048] text-white px-5 py-1 rounded-2xl"> {event.event.category_name.name} </p>
        </div>
        <div class="mt-4 flex items-center space-x-2 max-sm:justify-center">
            <img src="/home/person.png" alt="" width="30">
            <p class="text-[#8E8B8B]"> {event.event.created_by.username} </p>
        </div>
        <img src="/home/activity.png" alt="" class="w-full mt-4">

        <div class="mt-6">
            <p class="text-3xl font-bold"> Description </p>
            <p class="mt-3 text-[#8E8B8B]"> {event.event.description}</p>
        </div>

        <div class="mt-6">
            <p class="text-3xl font-bold"> Location </p>
            <p class="mt-3 text-[#8E8B8B]"> {event.event.location} </p>
        </div>

        <div class="grid grid-cols-2 gap-3 mt-5 max-sm:flex max-sm:flex-col">
            <div class="flex items-center space-x-4">
                <img src="/home/time.png" alt="" width="50">
                <p class="text-xl"> {event.event.start_time} - {event.event.end_time} </p>
            </div>
            <div class="flex items-center space-x-4">
                <img src="/home/people.png" alt="" width="50">
                <p class="text-3xl"> {event.event.max_capacity} </p>
            </div>
        </div>

        <div class="max-sm:flex max-sm:flex-col max-sm:gap-0">
            <button class="w-full max-sm:my-2 shadow-md my-5 py-3 border-2 text-[#8E8B8B] font-bold text-xl hover:bg-[#f1f1f1] duration-200 rounded-lg" onclick={closeInfoModal}>
            Close
            </button>
            <!-- <button class="max-sm:w-full max-sm:my-2 shadow-md my-5 py-3 text-white bg-[#FFB97C] font-bold text-xl hover:bg-[#d89458] duration-200 rounded-lg">
            Join us 
            </button> -->
        </div>
    </section>
</div>
{/if}

{#if isQrModalShow}
<div class="fixed inset-0 flex items-center justify-center z-50">
    
    <section class="w-[26%] font-semibold shadow-md overflow-y-auto bg-[#f8f8f8] max-lg:w-[90%] max-sm:mt-30">
        <div class="p-7 bg-blue-500">
            <h1 class="text-2xl text-white font-semibold text-center"> Plant a tree </h1>
        </div>
        
        <div>
            <div class="flex flex-col items-center space-y-5">
                <img src={qrDataUrl} alt="" width="200" class="shadow-lg rounded-lg mt-3">
                <p class="font-bold"> Ticket code </p>
                <p class="border-[#B0B0B0] w-[70%] text-center py-3 border-dashed border-2 rounded-lg mb-4"> {event.ticket_code}</p>
            </div>
        </div>

        <div class="border-t flex justify-center items-center py-3 mt-3 border-[#B0B0B0] border">
            <button class="text-[#A2A2A2] font-extrabold cursor-pointer" onclick={closeQrModal}> Close </button>
        </div>
    </section>
</div>
{/if}


