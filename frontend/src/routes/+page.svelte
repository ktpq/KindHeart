<script>
    export let data
    import HomeEvent from './HomeEvent.svelte';
    import { onMount } from 'svelte';
    import 'aos/dist/aos.css';
    import AOS from 'aos'

    let allEvent = data.allEvent
    let originalEvents = [...allEvent] 
    let searchText = ""

    onMount(() => {
        AOS.init();
    }) 

    const filterEvent = () => {
        const query = searchText.toLowerCase().trim()
        allEvent = query === "" ? [...originalEvents] : originalEvents.filter(event =>
            event.title.toLowerCase().includes(query)
        )
    }
</script>

<main class="bg-[#f0f4ff] min-h-screen p-6">
    <section class="w-full max-w-6xl mx-auto mt-8">
        <div class="flex justify-between items-center flex-wrap gap-4">
            <div class="relative flex-1">
                <input 
                    type="text" 
                    class="w-full bg-white py-3 pl-12 pr-4 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 font-medium text-gray-700" 
                    placeholder="Search Events" 
                    bind:value={searchText} 
                    oninput={filterEvent}
                >
                <img src="/home/search.png" alt="search icon" class="absolute top-1/2 left-3 -translate-y-1/2 w-6 h-6 opacity-60">
            </div>
        </div>

        <div class="mt-12 space-y-6">
            {#if data.isLogin}
                {#if allEvent.length > 0}
                    {#each allEvent as event}
                        <HomeEvent event={event}/>
                    {/each}
                {:else}
                    <p class="text-center text-gray-400 text-lg font-medium mt-10">
                        ไม่พบอีเวนต์ "{searchText}"
                    </p>
                {/if}
            {:else}
                <p class="text-center text-gray-400 text-lg font-medium mt-10">
                    กรุณาเข้าสู่ระบบเพื่อดูกิจกรรม
                </p>
            {/if}
        </div>
    </section>
</main>
