<script lang="ts">
    export let data
    import { goto } from '$app/navigation';
    import axios from 'axios';
    import Cookies from 'js-cookie';
    

    let file: File | null = null;
    
    
    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (selectedFile){
            file = selectedFile;
            previewUrl = URL.createObjectURL(selectedFile)
        }
    }

    const base_api = import.meta.env.VITE_API_URL

    let title = data.event.title
    let description = data.event.description
    let location = data.event.location
    let start_time = (data.event.start_time).slice(0,16)
    let end_time = (data.event.end_time).slice(0,16)
    let capacity = data.event.max_capacity
    let category = (data.event.category).toString()
    let previewUrl = `${base_api}${data.event.img_url}`
    
    const handleEdit = () => {
        
    }

   

</script>

<div class="flex items-center space-x-4">
    
    <img src="/create/message.png" alt="" width="50">
    <h1 class="text-4xl font-bold"> Edit Event</h1>
</div>
{JSON.stringify(data.event)}
<p class="text-[#99A799] text-3xl font-semibold mt-5"> Title </p>
<input type="text" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event title" bind:value={title}>

<p class="text-[#99A799] text-3xl font-semibold mt-5"> Description </p>
<textarea name="" id="" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD] h-[200px]" placeholder="Enter your description" bind:value={description}></textarea>

<p class="text-[#99A799] text-3xl font-semibold mt-5"> Location </p>
<input type="text" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event location" bind:value={location}>

<div class="grid grid-cols-3 gap-10 mt-5 max-md:grid-cols-1 max-md:gap-3">
    <div>
        <p class="text-[#99A799] text-3xl font-semibold mt-5"> Start time </p>
        <input type="datetime-local" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" bind:value={start_time}>
    </div>
    <div>
        <p class="text-[#99A799] text-3xl font-semibold mt-5"> End time </p>
        <input type="datetime-local" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" bind:value={end_time}>
    </div>
    <div>
        <p class="text-[#99A799] text-3xl font-semibold mt-5"> Capacity </p>
        <input type="text" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]" placeholder="Enter your event capacity" bind:value={capacity}>
    </div>
</div>

<p class="text-[#99A799] text-3xl font-semibold mt-5"> Category </p>
<select name="" id="" class="w-full mt-3 px-5 py-3 rounded-xl focus:outline-none bg-[#D3E4CD]"  bind:value={category}>
    <option value=""> select category </option>
    <option value="1" class="pr-10">สิ่งแวดล้อม </option>
    <option value="2" class="pr-10"> สังคมและชุมชน </option>
    <option value="3" class="pr-10"> การศึกษา </option>
    <option value="4" class="pr-10"> สุขภาพและการแพทย์ </option>
    <option value="5" class="pr-10"> จิตอาสาออนไลน์ </option>
</select>

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
        <button class="shadow-md px-6 py-3 cursor-pointer rounded-lg shadow-md text-white bg-[#32b04f] hover:bg-[#22923c] duration-200" onclick={handleEdit}>Create</button>
    </div>
</div>