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

<main class="bg-[#FEF5ED] min-h-screen p-5">
    <section class="w-[90%] mx-auto mt-5 max-lg:w-[100%]" data-aos="fade-up" data-aos-duration="1500">
		<div class="w-fit mx-auto mb-5 flex items-center space-x-4">
			<a href="/profile" class="px-5 py-2 rounded-2xl shadow-md text-white bg-[#ae67e7] hover:bg-[#8336c2] duration-200"> profile </a>
			<a href="/participation" class="px-5 py-2 rounded-2xl shadow-md bg-[#d2e4cc] hover:bg-[#aac2a3] duration-200"> participations </a>
			<a href="/myevents" class="px-5 py-2 rounded-2xl shadow-md bg-[#d2e4cc] hover:bg-[#aac2a3] duration-200"> my events </a>
		</div>
        <h1 class="text-[55px] font-semibold text-center"> Profile Settings </h1>
        <p class="text-[#ADC2A9] text-center text-[25px] mt-3 font-semibold"> Manage your account information </p>
        {@render children?.()}
    </section>

</main>

