<script>
	import '../../app.css';
	// import favicon from '$lib/assets/favicon.svg';
	import { page } from '$app/state';
	import Navbar from '$lib/Navbar.svelte';
	let { children } = $props();

    import { onMount } from 'svelte';
    import 'aos/dist/aos.css';
    import AOS from 'aos'
 
    onMount(() =>{
        AOS.init();
    })
</script>

<svelte:head>
	<!-- <link rel="icon" href={favicon} /> -->
</svelte:head>
<!-- {#if page.url.pathname !== "/" && page.url.pathname !== "/register"}
<Navbar/>
{/if} -->

<main class="bg-[#f0f4ff] min-h-screen p-5">
    <section class="w-[90%] mx-auto mt-5 max-lg:w-[100%]">
		
        {@render children?.()}
    </section>

</main>

