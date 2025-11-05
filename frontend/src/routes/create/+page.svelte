<script lang="ts">
    import axios from "axios";
    import Cookies from 'js-cookie'
    import { goto } from "$app/navigation";
    import Swal from 'sweetalert2';
    let file: File | null = null;
    let previewUrl = "";

    //@ts-ignore
    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (selectedFile){
            file = selectedFile;
            previewUrl = URL.createObjectURL(selectedFile)
        }
    }

    let title = ""
    let description = ""
    let location = ""
    let start_time = ""
    let end_time = ""
    let max_capacity = ""
    let category = ""
    
    const handleSubmit = async () => {
        try {
            const base_api = import.meta.env.VITE_API_URL
            const token = Cookies.get('authToken')

            if (title === "" || description === "" || location === "" || start_time === "" || end_time === "" || max_capacity === "" || category === "") {
                alert("กรุณากรอกข้อมูลให้ครบถ้วน")
                return
            }

            const startDate = new Date(start_time)
            const endDate = new Date(end_time)
            const now = new Date()
            if (endDate < startDate) {
                alert("End time ต้องมากกว่า Start time")
                return
            }
            if (now > endDate || now > startDate){
                alert("ไม่สามารถสร้าง event ในอดีตได้")
                return 
            }

            const formData = new FormData()
            formData.append("title", title)
            formData.append("description", description)
            formData.append("location", location)
            formData.append("start_time", start_time)
            formData.append("end_time", end_time)
            formData.append("max_capacity", max_capacity)
            formData.append("category", category)
            if (file) formData.append("img_url", file)

            await axios.post(`${base_api}/api/event/`, formData, {
                headers: { Authorization: `Token ${token}` }
            })

            Swal.fire({
                title: "สร้างกิจกรรมสำเร็จ!",
                icon: "success"
            })
            goto('/myevents')

        } catch (error) {
            console.log(error.response.data)
        }
    }
</script>

<div class="bg-white shadow-lg rounded-2xl p-8 max-w-4xl mx-auto mt-10">
    <div class="flex items-center space-x-4 mb-8">
        <img src="/create/message.png" alt="" width="50">
        <h1 class="text-4xl font-bold text-blue-600">Create Event</h1>
    </div>

    <!-- Title -->
    <div class="mb-5">
        <label class="text-blue-600 text-2xl font-semibold">Title</label>
        <input type="text" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" placeholder="Enter your event title" bind:value={title}>
    </div>

    <!-- Description -->
    <div class="mb-5">
        <label class="text-blue-600 text-2xl font-semibold">Description</label>
        <textarea class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm h-40" placeholder="Enter your description" bind:value={description}></textarea>
    </div>

    <!-- Location -->
    <div class="mb-5">
        <label class="text-blue-600 text-2xl font-semibold">Location</label>
        <input type="text" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" placeholder="Enter your event location" bind:value={location}>
    </div>

    <!-- Time & Capacity -->
    <div class="grid grid-cols-3 gap-6 mb-5 max-md:grid-cols-1">
        <div>
            <label class="text-blue-600 text-2xl font-semibold">Start Time</label>
            <input type="datetime-local" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" bind:value={start_time}>
        </div>
        <div>
            <label class="text-blue-600 text-2xl font-semibold">End Time</label>
            <input type="datetime-local" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" bind:value={end_time}>
        </div>
        <div>
            <label class="text-blue-600 text-2xl font-semibold">Capacity</label>
            <input type="text" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" placeholder="Enter your event capacity" bind:value={max_capacity}>
        </div>
    </div>

    <!-- Category -->
    <div class="mb-5">
        <label class="text-blue-600 text-2xl font-semibold">Category</label>
        <select class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" bind:value={category}>
            <option value="">Select category</option>
            <option value="1">Environment</option>
            <option value="2">Social & Community</option>
            <option value="3">Education</option>
            <option value="4">Health & Medical</option>
            <option value="5">Online Volunteering</option>
        </select>
    </div>

    <!-- Upload Image -->
    <div class="mb-5">
        <label class="text-blue-600 text-2xl font-semibold mb-2 block">Upload Image</label>
        <div class="flex items-center space-x-5">
            {#if previewUrl}
                <label for="file" class="px-5 py-2 bg-red-500 text-white rounded-lg shadow-md cursor-pointer hover:bg-red-600 transition font-bold">
                    Change Image
                </label>
            {/if}
        </div>
        <input type="file" id="file" class="hidden" accept="image/*" onchange={handleFileChange}/>
        <div class="mt-3 border-2 border-dashed border-blue-200 rounded-2xl h-40 flex justify-center items-center bg-blue-50 shadow-sm">
            {#if !previewUrl}
                <label for="file" class="text-blue-400 font-semibold cursor-pointer">Add Image</label>
            {/if}
            {#if previewUrl}
                <img src={previewUrl} alt="preview" class="w-[150px] h-[150px] object-contain rounded-lg"/>
            {/if}
        </div>
    </div>

    <!-- Buttons -->
    <div class="flex justify-end mt-8 space-x-4">
        <a href="/myevents" class="px-6 py-3 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 transition font-bold">Cancel</a>
        <button class="px-6 py-3 bg-green-500 text-white rounded-lg shadow-md hover:bg-green-600 transition font-bold" onclick={handleSubmit}>Create</button>
    </div>
</div>
