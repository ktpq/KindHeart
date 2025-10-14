<script>
	import Cookies from 'js-cookie'
	import { goto } from '$app/navigation';
	let isOpen = $state(false);
	let isDropDownOpen = $state(false);

	import { user } from '../stores';

	const toggleDropdown = () => {
		isDropDownOpen = !isDropDownOpen;
	};

	const handleLogout = () => {
		Cookies.remove('authToken')
		user.set(null)
		goto('/login')
	}
</script>

<nav class="bg-white shadow-md p-5">
	<section class="w-full max-w-6xl mx-auto flex justify-between items-center">
		<a href="/" class="font-bold text-3xl text-blue-600">
			KindHeart 🩷
		</a>

		<!-- Desktop Menu -->
		<div class="flex items-center space-x-6 min-w-[250px] hidden lg:flex relative">
			{#if $user}
				<a href="/notification" class="relative">
					<!-- Bell SVG -->
					<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-blue-500 hover:text-blue-600 transition" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6 6 0 10-12 0v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
					</svg>
				</a>

				<div class="relative">
					<button onclick={toggleDropdown} class="flex items-center space-x-2 focus:outline-none">
						<p class="text-gray-700 font-semibold text-lg">{$user.username}</p>
						<svg xmlns="http://www.w3.org/2000/svg" class={`w-6 h-6 text-blue-500 transition-transform duration-200 ${isDropDownOpen ? 'rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
						  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
						</svg>
					</button>

					{#if isDropDownOpen}
						<div class="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded-lg shadow-lg z-50 animate-fade-in">
							<a href="/profile" class="block px-4 py-2 hover:bg-blue-50 text-gray-700">Profile</a>
							{#if $user.is_staff}
								<a href="/admin" class="block px-4 py-2 hover:bg-blue-50 text-gray-700">Admin Panel</a>
							{/if}
							<button class="w-full text-left block px-4 py-2 hover:bg-blue-50 text-red-500" onclick={handleLogout}>Logout</button>
						</div>
					{/if}
				</div>
			{:else}
				<a href="/login" class="h-10 px-6 rounded-lg bg-blue-50 text-blue-600 font-semibold flex items-center justify-center hover:bg-blue-100 transition">
					Login
				</a>
			{/if}
		</div>

		<!-- Mobile Hamburger -->
		<button class="lg:hidden" onclick={() => isOpen = !isOpen}>
			<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
			  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
			</svg>
		</button>
	</section>
</nav>

<!-- Mobile Menu -->
{#if isOpen}
	<div class="lg:hidden bg-white border-t border-gray-200 p-5 animate-fade-in">
		{#if $user}
			<div class="flex items-center justify-between">
				<a href="/notification">
					<svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6 6 0 10-12 0v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
					</svg>
				</a>
				<button onclick={toggleDropdown} class="flex items-center space-x-2 focus:outline-none">
					<p class="text-gray-700 font-semibold">{$user.username}</p>
					<svg xmlns="http://www.w3.org/2000/svg" class={`w-6 h-6 text-blue-500 transition-transform duration-200 ${isDropDownOpen ? 'rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
					  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
					</svg>
				</button>
			</div>

			{#if isDropDownOpen}
				<div class="mt-3 bg-blue-50 border border-gray-200 rounded-lg shadow-md">
					<a href="/profile" class="block px-4 py-2 hover:bg-blue-100 text-gray-700">Profile</a>
					<a href="/admin" class="block px-4 py-2 hover:bg-blue-100 text-gray-700">Admin Panel</a>
					<button class="block px-4 py-2 hover:bg-blue-100 text-red-500 w-full text-left" onclick={handleLogout}>Logout</button>
				</div>
			{/if}
		{:else}
			<a href="/login" class="block w-full text-center h-10 rounded-lg bg-blue-50 text-blue-600 font-semibold hover:bg-blue-100 transition mt-2">
				Login
			</a>
		{/if}
	</div>
{/if}

<style>
	@keyframes fade-in { from { opacity: 0; transform: translateY(-5px);} to {opacity:1; transform:translateY(0);} }
	.animate-fade-in { animation: fade-in 0.2s ease-out; }
</style>
