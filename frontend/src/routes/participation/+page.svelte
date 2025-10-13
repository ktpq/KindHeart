<script>
    import ParticipationEvent from "./ParticipationEvent.svelte";
    export let data
    let events = [
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
    ]

    let allEvent = data.allEvent
</script>

<div class="w-[100%] mx-auto p-5">
    <!-- {JSON.stringify(data)} -->
    {#each allEvent as event}
    <ParticipationEvent event ={event}/>
    {/each}
</div>