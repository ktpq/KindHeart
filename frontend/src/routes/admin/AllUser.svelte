<script>
    import UserCard from "./UserCard.svelte";
    let allUser = $state([
		{
			id: 1,
			username: "johndoe",
			email: "johndoe@example.com"
		},
		{
			id: 2,
			username: "janesmith",
			email: "janesmith@example.com"
		},
		{
			id: 3,
			username: "mikebrown",
			email: "mikebrown@example.com"
		}
	]);
</script>

<section>
    {#each allUser as user}
    <UserCard user={user}/> 
    {/each}

    
</section>


