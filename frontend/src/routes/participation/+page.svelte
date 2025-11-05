<script>
    import ParticipationEvent from "./ParticipationEvent.svelte";
    export let data;

    let allEvent = data.allEvent || [];
</script>

<div class="w-[100%] mx-auto p-5 space-y-4">
    {#if allEvent.length === 0}
        <div class="text-center text-blue-800 text-xl font-semibold py-10 bg-blue-50 rounded-lg shadow-md">
            No participations yet.
        </div>
    {/if}

    {#each allEvent as event}
        <ParticipationEvent event={event} />
    {/each}
</div>
