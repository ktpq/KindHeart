<script>
    import { onMount } from 'svelte';
    import 'aos/dist/aos.css';
    import AOS from 'aos'
    import axios from 'axios'
    import Cookies from 'js-cookie'
    import { goto } from '$app/navigation';
    import { user } from '../../stores';
 
    onMount(() =>{
        AOS.init();
    })

    let username = $state()
    let password = $state()

    const handleSignin = async () => {
      try {
          const base_api = import.meta.env.VITE_API_URL
          const response = await axios.post(`${base_api}/api-token-auth/`, {username: username, password: password})
          const token = response.data.token
          Cookies.set('authToken', token, {expires: 7})

          const responseUser = await axios.get(`${base_api}/api/auth/myprofile`,{
              headers: { Authorization: `Token ${token}`}
          })
          user.set(responseUser.data)
          alert("ล็อคอินสำเร็จ !")
          goto('/')
      } catch (error){
          if (error){
            alert("username หรือ password ผิด")
          }
         
      }
    }

</script>

<main class="bg-[#FEF5ED] h-screen flex justify-center items-center">
  
  <section class="grid grid-cols-2 w-[65vw] max-xl:w-full max-xl:grid-cols-1">
    <div class="px-25 flex flex-col items-center justify-center max-lg:px-15 max-sm:px-5"  data-aos="fade-up" data-aos-duration="1500">
      <h1 class="text-5xl font-semibold mb-5 text-center">Login</h1>

      <div class="my-4 w-full relative">
        <img src="./login/email-green.png" alt="" class="absolute left-1 top-3">
        <input type="text" placeholder="Username" class="focus:outline-none py-3 border-b-2 border-[#D3E4CD] pl-10 pr-5 text-[#bad8af] w-[100%] font-semibold" bind:value={username}/>
      </div>

      <div class="my-4 w-full relative">
        <img src="./login/password-green.png" alt="" class="absolute left-1 top-3">
        <input type="password" placeholder="Password" class="focus:outline-none py-3 border-b-2 border-[#D3E4CD] pl-10 pr-5 text-[#bad8af] w-[100%] font-semibold" bind:value={password}/>
      </div>
      <button class="px-14 py-3 text-lg my-5 bg-[#ADC2A9] font-semibold text-white rounded-4xl hover:bg-[#99a798] duration-200" onclick={handleSignin}> Sign in</button>
      <p class="text-[#99A799] font-semibold text-lg my-3"> Don't have an account ?  <a href="/register" class="text-[#FFB97C]"> Register </a></p>
    </div>

    <!-- เอาไว้ใส่ภาพ -->
    <div class="max-xl:hidden" data-aos="fade-up" data-aos-duration="1500">
      <img src="./login/image.png" alt="">
    </div>

  </section>
</main>
