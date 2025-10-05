<script>
    let { noti } = $props()
</script>

<div class="bg-[#aec2a9]/10 p-7 my-5 shadow-md rounded-xl border border-[#aec2a9] hover:shadow-lg hover:-translate-y-1 duration-200 cursor-pointer">
    <div class="flex items-center justify-between">
        <div class="flex items-center space-x-5">
            <img src="/notification/green-bell.png" alt="" width="30">
            <p class="text-xl font-semibold"> {noti.title}</p>
        </div>
        <button class="cursor-pointer hover:bg-[#d2e4cc] duration-200 rounded-[100%]"> <img src="/notification/red-trash.png" alt="" class="p-1" width="40"> </button>
    </div>
    <p class="ml-13 mt-2 text-gray-500"> {noti.description} </p>
    <p class="ml-13 mt-2 text-gray-500"> {noti.date} </p>
    
</div>