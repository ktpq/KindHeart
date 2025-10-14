<script>
	import '../../app.css';
	import Navbar from '$lib/Navbar.svelte';
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import 'aos/dist/aos.css';
	import AOS from 'aos';

	let { children } = $props();

	onMount(() => {
		AOS.init();
	});

	const tabs = [
		{ name: 'Profile', href: '/profile' },
		{ name: 'Participations', href: '/participation' },
		{ name: 'My Events', href: '/myevents' }
	];

	const isActive = (href) => page.url.pathname === href;
</script>

<svelte:head>
	<title>KindHeart Account</title>
</svelte:head>

<!-- Navbar -->

<main class="bg-[#f0f4ff] min-h-screen p-5">
    <section class="w-[90%] mx-auto mt-5 max-lg:w-[100%]">

		<!-- Tabs for Profile, Participation, MyEvents -->
		<div class="w-fit mx-auto mb-8 flex items-center space-x-4 max-sm:space-x-2">
			{#each tabs as tab}
				<a 
					href={tab.href} 
					class="px-5 py-2 rounded-2xl shadow-md font-semibold transition duration-200
						{isActive(tab.href) 
							? 'bg-blue-600 text-white hover:bg-blue-700' 
							: 'bg-blue-100 text-blue-800 hover:bg-blue-200'}">
					{tab.name}
				</a>
			{/each}
		</div>

        <!-- Page Header -->
        <h1 class="text-[48px] font-bold text-center text-blue-900 mb-2">Account Settings 🩷</h1>
        <p class="text-blue-700 text-center text-lg mb-10">Manage your account information securely</p>

        <!-- Render the page content -->
        <div class="mt-10">
			{@render children?.()}
		</div>
    </section>
</main>

<style>
	@keyframes fade-in {
		from { opacity: 0; transform: translateY(-5px); }
		to { opacity: 1; transform: translateY(0); }
	}
	/* .animate-fade-in {
		animation: fade-in 0.2s ease-out;
	} */
</style>
