<script>
    let { user } = $props()
</script>

<div class="bg-white flex justify-between items-center p-5 shadow-md rounded-xl hover:-translate-y-1 duration-200 my-3 max-md:flex-col max-md:space-y-3">
    <div>
        <h2 class="text-xl font-bold"> {user.username} </h2>
        <h3 class="text-lg font-semibold mt-2 text-[#ADC2A9]"> {user.email} </h3>
    </div>
    <div class="flex items-center space-x-3">
        <a class="px-5 py-2 text-xl font-semibold  border-gray-200 hover:bg-[#d3d2d2] duration-200 rounded-xl shadow-md cursor-pointer" href="/user/{user.id}"> View profile </a>
        <button class="px-5 py-2 text-white text-xl font-semibold bg-[#FE9A9C] hover:bg-[#ce6668] duration-200 rounded-xl shadow-md cursor-pointer"> Ban </button>
    </div>
</div>