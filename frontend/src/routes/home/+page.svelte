<script>
    import HomeEvent from "./HomeEvent.svelte";
    import { onMount } from 'svelte';
    import 'aos/dist/aos.css';
    import AOS from 'aos'
 
    onMount(() =>{
        AOS.init();
    })

    let events = $state([
    {
        id: 1,
        date: "3 December 2025",
        title: "Plant the tree",
        location: "Chonburi",
        start_time: "11AM",
        end_time: "4PM",
        category: "Environment",
        description: "ช่วยกันปลูกต้นไม้เพื่อเพิ่มพื้นที่สีเขียวในชุมชน",
        capacity: 25,
        author: "Ronnie Coleman"
    },
    {
        id: 2,
        date: "10 December 2025",
        title: "Beach Cleanup",
        location: "Pattaya",
        start_time: "8AM",
        end_time: "12PM",
        category: "Environment",
        description: "ร่วมทำความสะอาดชายหาดและอนุรักษ์สิ่งแวดล้อม",
        capacity: 40,
        author: "Lisa Smith"
    },
    {
        id: 3,
        date: "15 January 2026",
        title: "Charity Run",
        location: "Bangkok",
        start_time: "6AM",
        end_time: "10AM",
        category: "Sports",
        description: "วิ่งการกุศลเพื่อสนับสนุนเด็กนักเรียน",
        capacity: 100,
        author: "John Doe"
    },
    {
        id: 4,
        date: "20 February 2026",
        title: "Book Fair",
        location: "Chiang Mai",
        start_time: "9AM",
        end_time: "6PM",
        category: "Education",
        description: "งานแสดงหนังสือและกิจกรรมการเรียนรู้สำหรับทุกเพศทุกวัย",
        capacity: 75,
        author: "Mary Johnson"
    },
    {
        id: 5,
        date: "5 March 2026",
        title: "Art Workshop",
        location: "Khon Kaen",
        start_time: "1PM",
        end_time: "5PM",
        category: "Art",
        description: "เวิร์กชอปศิลปะสำหรับผู้เริ่มต้นและผู้สนใจงานศิลป์",
        capacity: 20,
        author: "Alice Brown"
    },
    {
        id: 6,
        date: "18 April 2026",
        title: "Music Festival",
        location: "Phuket",
        start_time: "2PM",
        end_time: "11PM",
        category: "Music",
        description: "เทศกาลดนตรีสดกับศิลปินชั้นนำหลายวง",
        capacity: 500,
        author: "David Lee"
    }
])



</script>

<main class="bg-[#FEF5ED] min-h-screen p-5">
    <section class="w-[90%] mx-auto mt-5">

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

            <!-- event component -->
            {#each events as event}
            <HomeEvent event={event}/>
            {/each}

            
        </div>
    </section>

</main>

 <!-- h-[800px] overflow-y-auto -->

