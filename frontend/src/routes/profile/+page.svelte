<script>
    import { user } from "../../stores";
    import axios from "axios";
    import { derived } from "svelte/store";
    import { goto } from "$app/navigation";
    import Cookies from 'js-cookie'
    
    // change profile information section
    let username = ""
    let email = ""

    $: if ($user) {
        username = $user?.username
        email = $user?.email
    }


    const handleChangeProfile = async () => {
        try{
            const base_api = import.meta.env.VITE_API_URL
            const response = await axios.put(`${base_api}/api/user/${$user?.id}/`, {username, email})
            alert("อัพเดตข้อมูลสำเร็จ")
        } catch (error){
            alert("ใส่อีเมล์ไม่ถูกต้องตามหลัก")
        }
    }

    let currentPassword = ""
    let newPassword = ""
    let netPasswordConfirm = ""

    const handleChangePassword = async () => {
        if (newPassword !== netPasswordConfirm){
            alert("รหัสผ่านใหม่ กับ ช่องยืนยันรหัสผ่านใหม่ไม่ตรงกัน !")
        } else {
            try{
                const base_api = import.meta.env.VITE_API_URL
                const token = Cookies.get('authToken')
                const response = await axios.put(`${base_api}/api/user/change-password/${$user?.id}/`, 
                    {current_password: currentPassword, new_password: newPassword}, 
                    { headers: {Authorization: `Token ${token}`}}
                )
                alert("เปลี่ยนรหัสผ่านสำเร็จ กรุณาล็อคอินใหม่อีกครั้ง")
                Cookies.remove('authToken')
                goto('/login')
                
                
            } catch (err){
                console.log(err)
            }
        }
    }

</script>
<div class="mt-10 w-[70%] mx-auto grid grid-cols-2 p-5 gap-10 max-lg:flex max-lg:flex-col max-lg:w-[93%]">
    <!-- box ซ้าย -->
    <div class="w-full">
        <div class="flex space-x-8 max-lg:flex-col">
            <!-- <img src="/profile/handsome.jpg" alt="" height="100" width="100" class="rounded-[100%] max-lg:mx-auto"> -->
            <div>
                <h1 class="text-3xl font-bold mb-3 max-lg:text-center"> Profile Information </h1>
                <div class="max-lg:flex max-lg:justify-center max-lg:space-x-3">
                    <!-- <input type="file" id="file" class="hidden" />
                    
                    <label for="file" class="px-5 py-2 border cursor-pointer bg-[#AD67E7] text-white duration-200 hover:bg-[#8844c0]">
                        Choose file
                    </label> -->
                </div>
            </div>
        </div>


        <p class="mt-10 text-2xl font-semibold text-[#99A799]"> Username </p>
        <div class="relative">
            <img src="/login/user-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="text" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" bind:value={username}>
        </div>

        <p class="mt-5 text-2xl font-semibold text-[#99A799]"> Email </p>
        <div class="relative">
            <img src="/login/email-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="text" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" bind:value={email}>
        </div>

        <button class="mt-5 py-2 bg-[#AD67E7] text-white font-semibold rounded-lg duration-200 hover:bg-[#8844c0] cursor-pointer flex items-center w-full justify-center space-x-3 shadow-md" onclick={handleChangeProfile}>
            <img src="/profile/white-save.png" alt="" width="30">
            <p> Save Changes </p>
        </button>
        
    </div>
    <!-- box ขวา -->
    <div>
        <h1 class="text-3xl font-bold mb-3"> Change Password </h1>
        <p class="text-[#ADC2A9] font-semibold]"> Update your password to keep your account secure </p>

        <p class="mt-10 text-2xl font-semibold text-[#99A799]"> Current Password </p>
        <div class="relative">
            <img src="/login/password-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="password" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" placeholder="Enter current password" bind:value={currentPassword}>
        </div>

        <p class="mt-10 text-2xl font-semibold text-[#99A799]"> New Password </p>
        <div class="relative">
            <img src="/login/password-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="password" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" placeholder="Enter new password" bind:value={newPassword}>
        </div>

        <p class="mt-5 text-2xl font-semibold text-[#99A799]"> Confirm New Password </p>
        <div class="relative">
            <img src="/login/password-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="password" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" placeholder="Enter confirm new password" bind:value={netPasswordConfirm}>
        </div>

        <button class="shadow-md mt-5 py-2 bg-[#AD67E7] text-white font-semibold rounded-lg duration-200 hover:bg-[#8844c0] cursor-pointer flex items-center w-full justify-center space-x-3" onclick={handleChangePassword}>
            <img src="/profile/white-lock.png" alt="" width="30">
            <p> Update Password </p>
        </button>
    </div>
</div>
