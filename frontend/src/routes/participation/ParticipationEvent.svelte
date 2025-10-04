<script>
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

    
</script>

<div class="border-t-4 border-[#D3E4CD] p-5 flex justify-between items-center my-4 max-lg:flex-col">
    <!-- box ซ้าย -->
    <div class="py-2 flex items-center justify-between space-x-8 max-lg:flex-col max-lg:space-x-0 max-lg:space-y-4">
        
        <p class="text-2xl font-semibold">{event.date} </p>
        
        <img src="/home/activity.png" alt="" class="min-w-[100px]" width="150">
        <div>
            <div class="flex items-center space-x-3 max-sm:flex-col max-sm:space-y-3">
                <p class="text-3xl font-bold font-main"> {event.title}  </p> 
                <p class="text-lg px-4 py-1 bg-[#BCF5C5] text-[#00E043] rounded-3xl"> success </p>
            </div>
            <div class="flex items-center space-x-4 mt-3 ">
                <img src="/home/location.png" alt="" width="30">
                <p class="text-xl font-semibold text-[#ADC2A9]"> {event.location} • {event.start_time} - {event.end_time} </p>
            </div>
        </div>
    </div>
    <!-- box ขวา -->
    <div class="flex flex-col justify-center space-y-3 max-lg:mt-5">
        <button class="bg-[#FFB97C] px-5 text-xl py-3 text-white rounded-lg font-bold hover:bg-[#ee9e59] duration-200 cursor-pointer "> Qr Code </button>
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
            <p class="bg-[#1AD048] text-white px-5 py-1 rounded-2xl"> {event.category} </p>
        </div>
        <div class="mt-4 flex items-center space-x-2 max-sm:justify-center">
            <img src="/home/person.png" alt="" width="30">
            <p class="text-[#8E8B8B]"> {event.author} </p>
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
            <div class="flex items-center space-x-4">
                <img src="/home/time.png" alt="" width="50">
                <p class="text-3xl"> {event.start_time} - {event.end_time} </p>
            </div>
            <div class="flex items-center space-x-4">
                <img src="/home/people.png" alt="" width="50">
                <p class="text-3xl"> {event.capacity} </p>
            </div>
        </div>

        <div class="max-sm:flex max-sm:flex-col max-sm:gap-0">
            <button class="w-full max-sm:my-2 shadow-md my-5 py-3 border-2 text-[#8E8B8B] font-bold text-xl hover:bg-[#f1f1f1] duration-200 rounded-lg" onclick={closeModal}>
            Close
            </button>
            <!-- <button class="max-sm:w-full max-sm:my-2 shadow-md my-5 py-3 text-white bg-[#FFB97C] font-bold text-xl hover:bg-[#d89458] duration-200 rounded-lg">
            Join us 
            </button> -->
        </div>
    </section>
</div>
{/if}


