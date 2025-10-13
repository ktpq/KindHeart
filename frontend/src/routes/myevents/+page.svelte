<script>
    import MyEvent from "./MyEvent.svelte";

    export let data; // จะได้จาก +page.js
    let events = data.events || [];
</script>

<div class="w-full p-5">
    <div class="flex justify-between items-center">
        <p></p>
        <a href="/create" class="bg-[#AD67E7] text-white px-5 py-3 rounded-lg hover:bg-[#5e268d]">Create Event</a>
    </div>

    {#if events.length === 0}
        <p class="mt-5 text-center text-2xl"> Loading...</p>
    {:else}
        {#each events as event}
            <MyEvent {event} />
        {/each}
    {/if}
</div>

