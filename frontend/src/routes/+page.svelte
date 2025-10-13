<script>
    export let data
    import HomeEvent from './HomeEvent.svelte';
    import { onMount } from 'svelte';
    import 'aos/dist/aos.css';
    import AOS from 'aos'
    let allEvent = data.allEvent
    onMount(() =>{
        AOS.init();
    }) 


    

</script>

<main class="bg-[#FEF5ED] min-h-screen p-5">
    <section class="w-[90%] mx-auto mt-5">
        {JSON.stringify(data)}
        <div class="flex justify-between items-center max-lg:flex-col">
            <div class="flex space-x-3 max-lg:flex-col max-lg:w-full max-lg:space-y-3">
                <div class="relative max-lg:w-full">
                    <input type="text" class="bg-[#ADC2A9] py-3 pr-5 pl-12 border-2 border-[#D3E4CD] rounded-lg focus:outline-none font-bold max-lg:w-[100%]" placeholder="Search Events">
                    <img src="/home/search.png" alt="" width="25" class="absolute top-3 left-2">
                </div>
                <select name="" id="" class="bg-[#ADC2A9] py-3 px-5 rounded-lg border-2 border-[#D3E4CD] focus:outline-none font-bold">
                    <option value="All Events">All Events </option>
                    <option value="ex1"> Ex1 </option>
                </select>
            </div>

            <select name="" id="" class="bg-[#ADC2A9] py-3 px-5 rounded-lg border-2 border-[#D3E4CD] focus:outline-none font-bold max-lg:w-full max-lg:mt-2">
                <option value="Newest">Newest </option>
                <option value="Oldest"> Oldest </option>
            </select>
        </div>

        <div class="mt-10">

           
            {#each allEvent as event}
            <HomeEvent event={event}/>
            {/each}

            
        </div>
    </section>

</main>

 <!-- h-[800px] overflow-y-auto -->

