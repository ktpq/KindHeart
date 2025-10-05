<script>
    let file = null
    let previewUrl = "";
    export let data
    //@ts-ignore
    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (selectedFile){
            file = selectedFile;
            previewUrl = URL.createObjectURL(selectedFile)
        }
    }
</script>

<div class="flex items-center space-x-4">
    <img src="/create/message.png" alt="" width="50">
    <h1 class="text-4xl font-bold"> Edit Event -> {data.id}</h1>
</div>

<p class="text-[#99A799] text-3xl font-semibold mt-5"> Title </p>
<input type="text" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event title">

<p class="text-[#99A799] text-3xl font-semibold mt-5"> Description </p>
<textarea name="" id="" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD] h-[200px]" placeholder="Enter your description"></textarea>

<p class="text-[#99A799] text-3xl font-semibold mt-5"> Location </p>
<input type="text" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event location">

<div class="grid grid-cols-3 gap-10 mt-5 max-md:grid-cols-1 max-md:gap-3">
    <div>
        <p class="text-[#99A799] text-3xl font-semibold mt-5"> Start time </p>
        <input type="datetime-local" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event title">
    </div>
    <div>
        <p class="text-[#99A799] text-3xl font-semibold mt-5"> End time </p>
        <input type="datetime-local" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event title">
    </div>
    <div>
        <p class="text-[#99A799] text-3xl font-semibold mt-5"> Capacity </p>
        <input type="text" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event capacity">
    </div>
</div>

<div class="flex items-center space-x-5 mt-10">
    <p class="text-[#99A799] text-3xl font-semibold"> Upload image </p>
    {#if previewUrl}
        <label for="file" class="px-5 py-1 border cursor-pointer bg-[#AD67E7] text-white duration-200 hover:bg-[#8844c0] font-bold">
            Change Image
        </label>
    {/if}

</div>


<div class="border-3 border-dashed border-[#D3E4CD] h-[150px] flex justify-center items-center mt-5 rounded-2xl">
    <input type="file" id="file" class="hidden" accept="image/*" onchange={handleFileChange}/>

    {#if !previewUrl}
		<label for="file" class="text-xl font-semibold text-[#]">
            Add Image
        </label>
	{/if}
    

    {#if previewUrl}
		<img src={previewUrl} alt="preview" class="mt-3 w-[150px] h-[150px] object-contain rounded-lg" />
	{/if}
</div>

<div class="flex items-center justify-between mt-10">
    <p></p>
    <div class="flex items-center space-x-4">
        <a class="shadow-md px-6 py-3 cursor-pointer rounded-lg shadow-md text-white bg-[#d33641] hover:bg-[#ac202a] duration-200" href="/myevents">Cancel</a>
        <button class="shadow-md px-6 py-3 cursor-pointer rounded-lg shadow-md text-white bg-[#32b04f] hover:bg-[#22923c] duration-200">Create</button>
    </div>
</div>