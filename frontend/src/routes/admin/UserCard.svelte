<script>
  import axios from "axios";
    let { user } = $props()
    import Swal from "sweetalert2";
    import Cookies from 'js-cookie'
    const base_api = import.meta.env.VITE_API_URL;
    const token = Cookies.get('authToken')
    
    const banUser = (user_id) => {
        Swal.fire({
        title: "Are you sure?",
        text: "คุณต้องการเปลี่ยนสิทธิ์ของผู้ใช้ใช่หรือไม่",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "ยืนยัน",
        cancelButtonText: "ยกเลิก",
        
        }).then(async (result) => {
        if (result.isConfirmed) {

            // ยิง api
            const response = await axios.put(`${base_api}/api/user/permission/${user_id}/`, {}, {
                headers: { Authorization: `Token ${token}`}
            })

            console.log(response)
            // window.location.href = "/admin"
            Swal.fire({
                title: "เปลี่ยนสิทธิ์ของผู้ใช้สำเร็จ!",
                icon: "success"
            }).then(() => {
                window.location.reload()
            })
            
        }
        });
    }
</script>

<div class="bg-white flex justify-between items-center p-5 shadow-md rounded-xl hover:-translate-y-1 duration-200 my-3 max-md:flex-col max-md:space-y-3">
    <div>
        <h2 class="text-xl font-bold"> {user.username} </h2>
        <h3 class="text-lg font-semibold mt-2 text-[#ADC2A9]"> {user.email} </h3>
    </div>
    <div class="flex items-center space-x-3">
        <a class="px-5 py-2 text-xl font-semibold  border-gray-200 hover:bg-[#d3d2d2] duration-200 rounded-xl shadow-md cursor-pointer" href="/user/{user.id}"> View profile </a>
        {#if user.is_active}
        <button class="px-5 py-2 text-white text-xl font-semibold bg-[#FE9A9C] hover:bg-[#ce6668] duration-200 rounded-xl shadow-md cursor-pointer" onclick={() => {banUser(user.id)}}> Ban </button>
        {:else}
        <button class="px-5 py-2 text-white text-xl font-semibold bg-[#3ac525] hover:bg-[#69ce66] duration-200 rounded-xl shadow-md cursor-pointer" onclick={() => {banUser(user.id)}}> unban </button>
        {/if}
    </div>
</div>