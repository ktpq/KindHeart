<script>
	import '../app.css';
	import { user, loadUser } from '../stores';
	import { onMount } from 'svelte';
	// import favicon from '$lib/assets/favicon.svg';
	import { page } from '$app/state';
	import Navbar from '$lib/Navbar.svelte';
	let { children } = $props();
	onMount(() =>{
		loadUser()
	})
	
</script>

<svelte:head>
	<!-- <link rel="icon" href={favicon} /> -->
</svelte:head>
{#if page.url.pathname !== "/login" && page.url.pathname !== "/register" && page.url.pathname !== "/admin"}
<Navbar/>
{/if}

{@render children?.()}
