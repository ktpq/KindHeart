<script>
    import MyEvent from "./MyEvent.svelte";

    export let data;
    let events = data.events || [];
</script>

<div class="w-full p-5">
    <!-- Header -->
    <div class="flex justify-between items-center mb-5 max-lg:flex-col max-lg:space-y-3">
        <h1 class="text-3xl font-bold text-blue-800">My Events</h1>
        <a href="/create" class="bg-blue-500 text-white px-5 py-3 rounded-lg font-bold hover:bg-blue-600 shadow-md duration-200 cursor-pointer">
            Create Event
        </a>
    </div>

    <!-- No Events -->
    {#if events.length === 0}
        <p class="mt-10 text-center text-2xl text-gray-400">ยังไม่มีอีเว้นท์.</p>
    {:else}
        <!-- Events List -->
        <div class="space-y-4">
            {#each events as event}
                <MyEvent {event} />
            {/each}
        </div>
    {/if}
</div>
