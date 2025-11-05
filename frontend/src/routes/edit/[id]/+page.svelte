<script lang="ts">
    export let data;
    import { goto } from '$app/navigation';
    import axios from 'axios';
    import Cookies from 'js-cookie';
    import Swal from 'sweetalert2';

    let file: File | null = null;
    const base_api = import.meta.env.VITE_API_URL;

    let title = data.event.title;
    let description = data.event.description;
    let location = data.event.location;
    let start_time = (data.event.start_time).slice(0,16);
    let end_time = (data.event.end_time).slice(0,16);
    let capacity = data.event.max_capacity;
    let category = (data.event.category).toString();
    let previewUrl = `${base_api}${data.event.img_url}`;

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (selectedFile){
            file = selectedFile;
            previewUrl = URL.createObjectURL(selectedFile);
        }
    };

    const handleEdit = async () => {
        try {
            const token = Cookies.get('authToken');

            if (!title || !description || !location || !start_time || !end_time || !capacity || !category) {
                return Swal.fire({
                    icon: 'warning',
                    title: 'กรุณากรอกข้อมูลให้ครบถ้วน'
                });
            }

            const startDate = new Date(start_time);
            const endDate = new Date(end_time);
            const now = new Date();

            if (endDate < startDate) {
                return Swal.fire({
                    icon: 'error',
                    title: 'End time ต้องมากกว่า Start time'
                });
            }

            if (now > endDate || now > startDate){
                return Swal.fire({
                    icon: 'error',
                    title: 'ไม่สามารถสร้าง event ในอดีตได้'
                });
            }

            const formData = new FormData();
            formData.append("title", title);
            formData.append("description", description);
            formData.append("location", location);
            formData.append("start_time", start_time);
            formData.append("end_time", end_time);
            formData.append("max_capacity", capacity);
            formData.append("category", category);
            if (file) formData.append("img_url", file);

            await axios.put(`${base_api}/api/event/${data.id}/`, formData, {
                headers :{ Authorization: `Token ${token}` }
            });

            await Swal.fire({
                icon: 'success',
                title: 'อัปเดตกิจกรรมสำเร็จ!',
                timer: 1500,
                showConfirmButton: false
            });

            goto('/myevents');
        } catch (error) {
            console.error(error);
            Swal.fire({
                icon: 'error',
                title: 'เกิดข้อผิดพลาดในการอัปเดต',
                text: error.message || ''
            });
        }
    };
</script>

<div class="bg-white shadow-lg rounded-2xl p-8 max-w-4xl mx-auto mt-10">
    <div class="flex items-center space-x-4 mb-8">
        <img src="/create/message.png" alt="" width="50">
        <h1 class="text-4xl font-bold text-blue-600">Edit Event</h1>
    </div>

    <!-- Title -->
    <div class="mb-5">
        <p class="text-blue-600 text-2xl font-semibold">Title</p>
        <input type="text" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" placeholder="Enter your event title" bind:value={title}>
    </div>

    <!-- Description -->
    <div class="mb-5">
        <p class="text-blue-600 text-2xl font-semibold">Description</p>
        <textarea class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm h-40" placeholder="Enter your description" bind:value={description}></textarea>
    </div>

    <!-- Location -->
    <div class="mb-5">
        <p class="text-blue-600 text-2xl font-semibold">Location</p>
        <input type="text" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" placeholder="Enter your event location" bind:value={location}>
    </div>

    <!-- Time & Capacity -->
    <div class="grid grid-cols-3 gap-6 mb-5 max-md:grid-cols-1">
        <div>
            <p class="text-blue-600 text-2xl font-semibold">Start Time</p>
            <input type="datetime-local" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" bind:value={start_time}>
        </div>
        <div>
            <p class="text-blue-600 text-2xl font-semibold">End Time</p>
            <input type="datetime-local" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" bind:value={end_time}>
        </div>
        <div>
            <p class="text-blue-600 text-2xl font-semibold">Capacity</p>
            <input type="text" class="w-full mt-2 px-5 py-3 rounded-xl focus:outline-none bg-blue-50 shadow-sm" placeholder="Enter your event capacity" bind:value={capacity}>
        </div>
    </div>

    <!-- Category -->
    <div class="mb-5">
        <p class="text-blue-600 text-2xl font-semibold">Category</p>
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
        <p class="text-blue-600 text-2xl font-semibold mb-2 block">Upload Image</p>
        <div class="flex items-center space-x-5">
            {#if previewUrl}
                <p class="px-5 py-2 bg-red-500 text-white rounded-lg shadow-md cursor-pointer hover:bg-red-600 transition font-bold">
                    Change Image
                </p>
            {/if}
        </div>
        <input type="file" id="file" class="hidden" accept="image/*" onchange={handleFileChange}/>
        <div class="mt-3 border-2 border-dashed border-blue-200 rounded-2xl h-40 flex justify-center items-center bg-blue-50 shadow-sm">
            {#if !previewUrl}
                <p class="text-blue-400 font-semibold cursor-pointer">Add Image</p>
            {/if}
            {#if previewUrl}
                <img src={previewUrl} alt="preview" class="w-[150px] h-[150px] object-contain rounded-lg"/>
            {/if}
        </div>
    </div>

    <!-- Buttons -->
    <div class="flex justify-end mt-8 space-x-4">
        <a href="/myevents" class="px-6 py-3 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 transition font-bold">Cancel</a>
        <button class="px-6 py-3 bg-green-500 text-white rounded-lg shadow-md hover:bg-green-600 transition font-bold" onclick={handleEdit}>Save</button>
    </div>
</div>
