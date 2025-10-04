<script>
    let isLogin = $state(false)
    let isOpen = $state(false)

</script>

<nav class="bg-[#D3E4CD] p-5">
    <section class="w-[90%] mx-auto flex justify-between items-center">
        <a href="/" class="font-semibold text-3xl text-[#FFB97C]">
            KindHeart
        </a>

        <!-- ฝั่งขวากำหนด min-w ไว้เพื่อกันเด้ง -->
        <div class="flex items-center justify-end min-w-[250px] max-md:hidden">
            {#if isLogin}
                <img src="/navbar/bell.png" alt="" width="35" class="cursor-pointer">
                <a class="flex items-center ml-7" href="">
                    <p class="text-[#99A799] font-bold text-xl text-shadow-sm"> kiwvy </p>
                    <img src="/navbar/drop-down.png" alt="" width="40">
                </a>
            {:else}
                <!-- ทำปุ่มให้สูงเท่ากับ icon -->
                <a href="/"
                   class="h-[40px] flex items-center border-3 px-7 rounded-xl bg-[#FEF5ED] border-[#ADC2A9] text-[#99A799] font-semibold text-xl">
                   Login
                </a>
            {/if}
        </div>

        <img src="/navbar/hamburger.png" alt="" width="35" class="hidden max-md:block" onclick={() => {isOpen = !isOpen}}>
    </section>
</nav>

{#if isOpen }
<div class="bg-[#D3E4CD] shadow-sm p-5 hidden max-md:block">
    {#if isLogin}
    <div class="flex item-center justify-around">
        <img src="/navbar/bell.png" alt="" width="35" class="cursor-pointer">
        <a class="flex items-center ml-7 text-[#99A799] font-bold text-xl text-shadow-sm" href="">
            Kiwvy
        </a>
        <a class="flex items-center ml-7 text-[#99A799] font-bold text-xl text-shadow-sm" href="">
            Logout
        </a>
    </div>
    {:else}
    <a href="/" class="h-[40px] text-center block w-full border-3 rounded-xl bg-[#FEF5ED] border-[#ADC2A9] text-[#99A799] font-semibold text-xl">
        Login
    </a>
    {/if}
    
</div>
{/if}




