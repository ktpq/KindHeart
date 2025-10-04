<script>
	import '../app.css';
	// import favicon from '$lib/assets/favicon.svg';
	import { page } from '$app/state';
	import Navbar from '$lib/Navbar.svelte';
	let { children } = $props();
</script>

<svelte:head>
	<!-- <link rel="icon" href={favicon} /> -->
</svelte:head>
{#if page.url.pathname !== "/" && page.url.pathname !== "/register"}
<Navbar/>
{/if}

{@render children?.()}
