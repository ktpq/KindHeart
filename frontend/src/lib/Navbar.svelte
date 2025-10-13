<script>
	import Cookies from 'js-cookie'
	import { goto } from '$app/navigation';
	let isLogin = $state(true);
	let isOpen = $state(false);
	let isDropDownOpen = $state(false);

	import { user } from '../stores';

	const toggleDropdown = () => {
		isDropDownOpen = !isDropDownOpen;
	};

	const handleLogout = () => {
		Cookies.remove('authToken')
		user.set(null)
		goto('/')
		// goto('/login')
	}
</script>

<nav class="bg-[#D3E4CD] p-5 relative shadow-sm">
	<section class="w-[90%] mx-auto flex justify-between items-center">
		<a href="/" class="font-semibold text-3xl text-[#FFB97C]">
			KindHeart
		</a>

		<!-- ฝั่งขวา (Desktop) -->
		<div class="flex items-center justify-end min-w-[250px] max-lg:hidden relative">
			{#if $user}
				<a href="/notification"><img src="/navbar/bell.png" alt="" width="35" class="cursor-pointer" /></a>
				<!-- {JSON.stringify($user)} -->
				<div class="ml-7 relative">
					<button
						onclick={toggleDropdown}
						class="flex items-center focus:outline-none cursor-pointer"
					>

						<p class="text-[#99A799] font-bold text-xl">{$user?.username}</p>
						<img
							src="/navbar/drop-down.png"
							alt=""
							width="40"
							class={`duration-200 transform ${isDropDownOpen ? "rotate-180" : ""}`}
						/>
					</button>

					{#if isDropDownOpen}
						<div
							class="absolute right-0 mt-2 w-48 bg-white border border-[#ADC2A9] rounded-lg shadow-lg z-50"
						>
							<a href="/profile" class="block px-4 py-2 hover:bg-[#D3E4CD] text-[#5E6D55]">Profile</a>
						    {#if $user.is_staff}
							<a href="/admin" class="block px-4 py-2 hover:bg-[#D3E4CD] text-[#5E6D55]">admin panel</a>
							{/if}
							<button class="block px-4 py-2 hover:bg-[#D3E4CD] text-[#d33641] w-full text-left" onclick={handleLogout}>Logout</button>
						</div>
					{/if}
				</div>
			{:else}
				<a
					href="/login"
					class="h-[40px] flex items-center px-7 rounded-xl bg-[#FEF5ED] border border-[#ADC2A9] text-[#99A799] font-semibold text-xl"
				>
					Login
				</a>
			{/if}
		</div>

		<!-- Hamburger -->
		<button class="hidden max-lg:block" onclick={() => (isOpen = !isOpen)}>
			<img src="/navbar/hamburger.png" alt="" width="35" />
		</button>
	</section>
</nav>

<!-- เมนูมือถือ -->
{#if isOpen}
	<div class="bg-[#D3E4CD] p-5 block lg:hidden border-t border-[#ADC2A9] animate-fade-in">
		{#if $user}
			<div class="flex items-center justify-between">
				<a href="/notification"><img src="/navbar/bell.png" alt="" width="30" class="cursor-pointer" /></a>
				<button
					onclick={toggleDropdown}
					class="flex items-center focus:outline-none"
				>
					<p class="text-[#99A799] font-bold text-xl mr-1">{$user.username}</p>
					<img
						src="/navbar/drop-down.png"
						alt=""
						width="30"
						class={`duration-200 transform ${isDropDownOpen ? "rotate-180" : ""}`}
					/>
				</button>
			</div>

			<!-- Dropdown (mobile) -->
			{#if isDropDownOpen}
				<div class="mt-3 bg-[#FEF5ED] border border-[#ADC2A9] rounded-lg shadow-md">
					<a href="/profile" class="block px-4 py-2 hover:bg-[#D3E4CD] text-[#5E6D55]">Profile</a>
					<a href="/admin" class="block px-4 py-2 hover:bg-[#D3E4CD] text-[#5E6D55]">admin panel</a>
					<button class="block px-4 py-2 hover:bg-[#D3E4CD] text-[#d33641]" onclick={handleLogout}>Logout</button>
				</div>
			{/if}
		{:else}
			<a
				href="/login"
				class="block w-full text-center h-[40px] mt-2 rounded-xl bg-[#FEF5ED] border border-[#ADC2A9] text-[#99A799] font-semibold text-xl"
			>
				Login
			</a>
		{/if}
	</div>
{/if}

<style>
	@keyframes fade-in {
		from {
			opacity: 0;
			transform: translateY(-5px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}
	.animate-fade-in {
		animation: fade-in 0.2s ease-out;
	}
</style>
