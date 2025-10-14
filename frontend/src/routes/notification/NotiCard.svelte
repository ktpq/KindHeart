<script>
	export let noti;
	export let index;

	// สีและไอคอน (SVG inline)
	const colors = [
		{
			border: "#f87171",
			bg: "#fee2e2",
			icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-7 h-7 text-[#b91c1c]">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m0 3.75h.008v.008H12V16.5zM21 12A9 9 0 1 1 3 12a9 9 0 0 1 18 0z" />
            </svg>`
		},
		{
			border: "#60a5fa",
			bg: "#dbeafe",
			icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-7 h-7 text-[#2563eb]">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m0 3.75h.008v.008H12V16.5zM12 9V6.75m0 12a9 9 0 1 1 0-18 9 9 0 0 1 0 18z" />
            </svg>`
		},
		{
			border: "#facc15",
			bg: "#fef9c3",
			icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" class="w-7 h-7 text-[#ca8a04]">
                <path d="M12 17.27l5.18 3.05-1.39-5.96L21 9.24l-6.09-.52L12 3 9.09 8.72 3 9.24l5.21 5.12L6.82 20.3z"/>
            </svg>`
		},
		{
			border: "#4ade80",
			bg: "#dcfce7",
			icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-7 h-7 text-[#15803d]">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
            </svg>`
		}
	];

	const theme = colors[index % colors.length];
</script>

<div
	class="p-6 my-5 shadow-md rounded-xl border hover:shadow-lg hover:-translate-y-1 duration-200 cursor-pointer"
	style="border-color:{theme.border}; background-color:{theme.bg}"
>
	<div class="flex items-center justify-between">
		<div class="flex items-center space-x-4">
			{@html theme.icon}
			<p class="text-lg font-semibold text-[#2f2f2f]">{noti.title}</p>
		</div>
	</div>
	<p class="ml-11 mt-2 text-gray-600">{noti.description}</p>
	<p class="ml-11 mt-1 text-sm text-gray-400">{noti.created_at_display}</p>
</div>
