<script>
    export let data
    import HomeEvent from './HomeEvent.svelte';
    import { onMount } from 'svelte';
    import 'aos/dist/aos.css';
    import AOS from 'aos'

    let allEvent = data.allEvent
    let originalEvents = [...allEvent] // เก็บสำเนาข้อมูลทั้งหมดไว้
    let searchText = ""

    onMount(() => {
        AOS.init();
    }) 

    const filterEvent = () => {
        const query = searchText.toLowerCase().trim()

        if (query === "") {
            allEvent = [...originalEvents] // ถ้าไม่มีข้อความ -> แสดงทั้งหมด
        } else {
            allEvent = originalEvents.filter(event =>
                event.title.toLowerCase().includes(query)
            )
        }
    }
</script>

<main class="bg-[#FEF5ED] min-h-screen p-5">
    <section class="w-[90%] mx-auto mt-5">
        <!-- {JSON.stringify(data)} -->
        <div class="flex justify-between items-center max-lg:flex-col">
            <div class="flex space-x-3 max-lg:flex-col max-lg:w-full max-lg:space-y-3">
                <div class="relative max-lg:w-full">
                    <input type="text" class="bg-[#ADC2A9] py-3 pr-5 pl-12 border-2 border-[#D3E4CD] rounded-lg focus:outline-none font-bold max-lg:w-[100%]" placeholder="Search Events" bind:value={searchText} oninput={filterEvent}>
                    <img src="/home/search.png" alt="" width="25" class="absolute top-3 left-2">
                </div>
                
            </div>
        </div>

        <div class="mt-10">
            {#if allEvent.length > 0}
                {#each allEvent as event}
                    <HomeEvent event={event}/>
                {/each}
            {:else}
                <p class="text-center text-gray-500 mt-10 text-xl font-semibold">
                    ไม่พบอีเวนต์ "{searchText}"
                </p>
            {/if}
        </div>
    </section>

</main>

 <!-- h-[800px] overflow-y-auto -->

