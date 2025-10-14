<script>
    import { user } from "../../stores";
    import axios from "axios";
    import { goto } from "$app/navigation";
    import Cookies from 'js-cookie'
    import Swal from 'sweetalert2'

    // Profile info
    let username = ""
    let email = ""
    $: if ($user) {
        username = $user?.username
        email = $user?.email
    }

    const handleChangeProfile = async () => {
        try {
            const base_api = import.meta.env.VITE_API_URL
            const token = Cookies.get('authToken')
            await axios.put(`${base_api}/api/user/${$user?.id}/`, {username, email}, {
                headers: { Authorization: `Token ${token}`}
            })
            Swal.fire({
                icon: 'success',
                title: 'Updated!',
                text: 'อัพเดตข้อมูลสำเร็จ',
                timer: 2000,
                showConfirmButton: false
            })
        } catch (error) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'ใส่อีเมล์ไม่ถูกต้องตามหลัก'
            })
        }
    }

    // Change password
    let currentPassword = ""
    let newPassword = ""
    let netPasswordConfirm = ""

    const handleChangePassword = async () => {
        if (newPassword !== netPasswordConfirm){
            Swal.fire({
                icon: 'warning',
                title: 'Mismatch!',
                text: 'รหัสผ่านใหม่ กับ ช่องยืนยันรหัสผ่านใหม่ไม่ตรงกัน !'
            })
            return
        } 
        try {
            const base_api = import.meta.env.VITE_API_URL
            const token = Cookies.get('authToken')
            await axios.put(`${base_api}/api/user/change-password/${$user?.id}/`, 
                {current_password: currentPassword, new_password: newPassword}, 
                { headers: {Authorization: `Token ${token}`} }
            )
            Swal.fire({
                icon: 'success',
                title: 'Password Updated!',
                text: 'เปลี่ยนรหัสผ่านสำเร็จ กรุณาล็อคอินใหม่',
                timer: 2500,
                showConfirmButton: false
            })
            Cookies.remove('authToken')
            goto('/login')
        } catch (err){
            console.log(err)
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'รหัสผ่านปัจจุบันไม่ถูกต้อง'
            })
        }
    }
</script>

<div class="mt-10 w-[70%] mx-auto grid grid-cols-2 gap-10 max-lg:flex max-lg:flex-col max-lg:w-[93%]">

    <!-- Profile Info -->
    <div class="w-full space-y-6 p-6 bg-white shadow-lg rounded-xl">
        <h1 class="text-3xl font-bold max-lg:text-center text-blue-900">Profile Information</h1>

        <p class="text-xl font-semibold text-blue-700">Username</p>
        <div class="relative shadow-sm rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 absolute top-3 left-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A9 9 0 1118.879 6.196 9 9 0 015.121 17.804z"/>
            </svg>
            <input type="text" class="pl-12 pr-5 py-2 bg-blue-50 rounded-lg w-full focus:outline-none text-lg" bind:value={username} />
        </div>

        <p class="text-xl font-semibold text-blue-700">Email</p>
        <div class="relative shadow-sm rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 absolute top-3 left-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12H8m0 0h8m-8 0V8m0 4v4"/>
            </svg>
            <input type="text" class="pl-12 pr-5 py-2 bg-blue-50 rounded-lg w-full focus:outline-none text-lg" bind:value={email} />
        </div>

        <button class="w-full flex items-center justify-center gap-3 py-3 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-md transition duration-200" on:click={handleChangeProfile}>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            <span>Save Changes</span>
        </button>
    </div>

    <!-- Change Password -->
    <div class="w-full space-y-6 p-6 bg-white shadow-lg rounded-xl">
        <h1 class="text-3xl font-bold max-lg:text-center text-blue-900">Change Password</h1>
        <p class="text-blue-700">Update your password to keep your account secure</p>

        <p class="text-xl font-semibold text-blue-700">Current Password</p>
        <div class="relative shadow-sm rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 absolute top-3 left-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 2.21-1.79 4-4 4s-4-1.79-4-4 1.79-4 4-4 4 1.79 4 4z"/>
            </svg>
            <input type="password" class="pl-12 pr-5 py-2 bg-blue-50 rounded-lg w-full focus:outline-none text-lg" placeholder="Enter current password" bind:value={currentPassword} />
        </div>

        <p class="text-xl font-semibold text-blue-700">New Password</p>
        <div class="relative shadow-sm rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 absolute top-3 left-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 2.21-1.79 4-4 4s-4-1.79-4-4 1.79-4 4-4 4 1.79 4 4z"/>
            </svg>
            <input type="password" class="pl-12 pr-5 py-2 bg-blue-50 rounded-lg w-full focus:outline-none text-lg" placeholder="Enter new password" bind:value={newPassword} />
        </div>

        <p class="text-xl font-semibold text-blue-700">Confirm New Password</p>
        <div class="relative shadow-sm rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 absolute top-3 left-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 2.21-1.79 4-4 4s-4-1.79-4-4 1.79-4 4-4 4 1.79 4 4z"/>
            </svg>
            <input type="password" class="pl-12 pr-5 py-2 bg-blue-50 rounded-lg w-full focus:outline-none text-lg" placeholder="Confirm new password" bind:value={netPasswordConfirm} />
        </div>

        <button class="w-full flex items-center justify-center gap-3 py-3 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-md transition duration-200" on:click={handleChangePassword}>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 2.21-1.79 4-4 4s-4-1.79-4-4 1.79-4 4-4 4 1.79 4 4z"/>
            </svg>
            <span>Update Password</span>
        </button>
    </div>
</div>
