<script>
    let { event } = $props()
    let isModalShow = $state(false)
</script>

<div class="bg-white flex justify-between items-center p-5 shadow-md rounded-xl hover:-translate-y-1 duration-200 my-3 max-md:flex-col max-md:space-y-3">
    <div>
        <h2 class="text-xl font-bold"> {event.title} </h2>
        <h3 class="text-lg font-semibold mt-2 text-[#ADC2A9]"> {event.date} </h3>
    </div>
    <div class="flex items-center space-x-3">
        <button class="px-5 py-2 text-xl font-semibold  border-gray-200 hover:bg-[#d3d2d2] duration-200 rounded-xl shadow-md cursor-pointer" onclick={() =>{isModalShow = !isModalShow}}> View info </button>
        <button class="px-5 py-2 text-white text-xl font-semibold bg-[#FE9A9C] hover:bg-[#ce6668] duration-200 rounded-xl shadow-md cursor-pointer"> Delete </button>
    </div>
</div>

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
            <button class="w-full max-sm:my-2 shadow-md my-5 py-3 border-2 text-[#8E8B8B] font-bold text-xl hover:bg-[#f1f1f1] duration-200 rounded-lg" onclick={() => {isModalShow = false}}>
            Close
            </button>
            <!-- <button class="max-sm:w-full max-sm:my-2 shadow-md my-5 py-3 text-white bg-[#FFB97C] font-bold text-xl hover:bg-[#d89458] duration-200 rounded-lg">
            Join us 
            </button> -->
        </div>
    </section>
</div>
{/if}