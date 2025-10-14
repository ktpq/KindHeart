<script>
    import UserCard from "./UserCard.svelte";
    let { allUser } = $props()
</script>

<section>
    {#each allUser as user}
    <UserCard user={user}/> 
    {/each}

    
</section>


