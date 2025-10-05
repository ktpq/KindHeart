<script>
    import NotiCard from "./NotiCard.svelte";

   let allNoti = $state([
		{
			id: 1,
			title: "System Maintenance",
			description: "The system will be under maintenance on October 10th from 1:00 AM to 3:00 AM.",
			date: "2025-10-10"
		},
		{
			id: 2,
			title: "New Event Available",
			description: "A new charity event has been added. Join now and make an impact!",
			date: "2025-10-08"
		},
		{
			id: 3,
			title: "Profile Update Reminder",
			description: "Please update your profile information to ensure we can contact you easily.",
			date: "2025-10-05"
		},
		{
			id: 4,
			title: "Thank You for Participating!",
			description: "We appreciate your participation in our recent event. Stay tuned for future updates.",
			date: "2025-10-02"
		}
	]);

</script>

<main>

    <section class="flex items-center space-x-5">

        <button class="cursor-pointer" onclick={() => {window.history.back()}}> <img src="/notification/green-back.png" alt=""> </button>
        

        <div class="">
            <div class="flex items-center space-x-3">
                <img src="/notification/green-bell.png" alt="" width="45">
                <h1 class="text-3xl text-[#99a798] font-semibold "> Notification </h1>
            </div>
            <p class="mt-3 font-semibold text-[#aec2a9]"> View your notification </p>
        </div>

    </section>

    <!-- notification -->
    <section>

        {#each allNoti as noti}
        <NotiCard noti={noti}/>
        {/each}
        

        


    </section>
    
</main>