<script>
	import NotiCard from "./NotiCard.svelte";
	export let data;

	let allNoti = data.allNoti;
</script>

<main class="p-8 bg-white min-h-screen">
	<!-- Header -->
	<section class="flex items-center space-x-5 mb-10">
		<button
			class="cursor-pointer text-blue-600 hover:text-blue-800 duration-200"
			onclick={() => window.history.back()}
		>
			<!-- Inline SVG แทน Iconify -->
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="2"
				stroke="currentColor"
				class="w-10 h-10"
			>
				<path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
			</svg>
		</button>

		<div>
			<div class="flex items-center space-x-3">
				<!-- Bell Icon -->
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="2"
					stroke="currentColor"
					class="w-10 h-10 text-blue-600"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M14.857 17.082a23.848 23.848 0 0 0 5.454-1.31A8.967 8.967 0 0 1 18 9V8a6 6 0 1 0-12 0v1a8.967 8.967 0 0 1-2.311 6.772c1.773.74 3.57 1.2 5.454 1.31m5.714 0a23.9 23.9 0 0 1-5.714 0m5.714 0a3 3 0 1 1-5.714 0"
					/>
				</svg>

				<h1 class="text-3xl text-blue-700 font-bold">Notifications</h1>
			</div>
			<p class="mt-2 font-medium text-blue-400">View your latest notifications</p>
		</div>
	</section>

	<!-- Notification list -->
	<section>
		{#if allNoti.length === 0}
			<p class="text-center text-gray-500 text-xl mt-20">
				No notifications available.
			</p>
		{:else}
			{#each allNoti as noti, i}
				<NotiCard noti={noti} index={i} />
			{/each}
		{/if}
	</section>
</main>
