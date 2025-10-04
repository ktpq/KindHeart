<script>
    
</script>
<div class="mt-10 w-[70%] mx-auto grid grid-cols-2 p-5 gap-10 max-lg:flex max-lg:flex-col max-lg:w-[93%]">
    <!-- box ซ้าย -->
    <div class="w-full">
        <div class="flex space-x-8 max-lg:flex-col">
            <img src="/profile/handsome.jpg" alt="" height="100" width="100" class="rounded-[100%] max-lg:mx-auto">
            <div>
                <h1 class="text-3xl font-bold mb-3 max-lg:text-center"> Profile Information </h1>

                <div class="max-lg:flex max-lg:justify-center max-lg:space-x-3">
                    <input type="file" id="file" class="hidden" />
                    <label for="file" class="px-5 py-2 border cursor-pointer bg-[#AD67E7] text-white duration-200 hover:bg-[#8844c0]">
                        Choose file
                    </label>
                    <button class="px-5 py-2 border bg-[#E76767] text-white duration-200 hover:bg-[#c54c4c]"> Delete </button>
                </div>
            </div>
        </div>


        <p class="mt-10 text-2xl font-semibold text-[#99A799]"> Username </p>
        <div class="relative">
            <img src="/login/user-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="text" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" value="johndoe">
        </div>

        <p class="mt-5 text-2xl font-semibold text-[#99A799]"> Email </p>
        <div class="relative">
            <img src="/login/email-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="text" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" value="johndoe@example.com">
        </div>

        <button class="mt-5 py-2 bg-[#AD67E7] text-white font-semibold rounded-lg duration-200 hover:bg-[#8844c0] cursor-pointer flex items-center w-full justify-center space-x-3 shadow-md">
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
            <input type="text" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" placeholder="Enter current password">
        </div>

        <p class="mt-10 text-2xl font-semibold text-[#99A799]"> New Password </p>
        <div class="relative">
            <img src="/login/password-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="text" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" placeholder="Enter new password">
        </div>

        <p class="mt-5 text-2xl font-semibold text-[#99A799]"> Confirm New Password </p>
        <div class="relative">
            <img src="/login/password-green.png" alt="" width="25" class="absolute top-5 left-2">
            <input type="text" class="pl-15 pr-5 py-2 mt-3 bg-[#D3E4CD] focus:outline-none text-xl w-full rounded-lg" placeholder="Enter confirm new password">
        </div>

        <button class="shadow-md mt-5 py-2 bg-[#AD67E7] text-white font-semibold rounded-lg duration-200 hover:bg-[#8844c0] cursor-pointer flex items-center w-full justify-center space-x-3">
            <img src="/profile/white-lock.png" alt="" width="30">
            <p> Update Password </p>
        </button>
    </div>
</div>
