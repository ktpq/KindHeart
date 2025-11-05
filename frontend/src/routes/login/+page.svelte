<script>
    import { onMount } from 'svelte';
    import 'aos/dist/aos.css';
    import AOS from 'aos'
    import axios from 'axios'
    import Cookies from 'js-cookie'
    import { goto } from '$app/navigation';
    import { user } from '../../stores';
    import Swal from 'sweetalert2';
 
    onMount(() =>{
        AOS.init();
    })

    let username = $state()
    let password = $state()

    const handleSignin = async () => {
      try {
          const base_api = import.meta.env.VITE_API_URL
          const response = await axios.post(`${base_api}/api-token-auth/`, {username, password})
          const token = response.data.token
          Cookies.set('authToken', token, {expires: 7})

          const responseUser = await axios.get(`${base_api}/api/auth/myprofile`,{
              headers: { Authorization: `Token ${token}`}
          })
          user.set(responseUser.data)

          Swal.fire({
            icon: 'success',
            title: 'ล็อคอินสำเร็จ!',
            text: `ยินดีต้อนรับ ${responseUser.data.username}`,
            confirmButtonColor: '#3B82F6'
          }).then(() => goto('/'))
          
      } catch (error){
          if (error.response.status == 400){
            Swal.fire({
              icon: 'error',
              title: 'เข้าสู่ระบบไม่สำเร็จ',
              text: 'กรุณาตรวจสอบ username และ password',
              confirmButtonColor: '#3B82F6'
            })
          }
      }
    }
</script>

<main class="bg-gray-50 h-screen flex justify-center items-center px-4">
  <section class="w-full max-w-md bg-white rounded-3xl shadow-2xl px-10 py-12" data-aos="fade-up" data-aos-duration="1500">
    <h1 class="text-4xl font-bold mb-8 text-center text-gray-800"> Login 🩷</h1>

    <div class="space-y-6">
      <!-- Username -->
      <div class="relative">
        <span class="absolute left-3 top-3 text-blue-500">
          <!-- Heroicons user icon -->
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.667 0 8 1.333 8 4v2H4v-2c0-2.667 5.333-4 8-4zm0-10a4 4 0 100 8 4 4 0 000-8z"/></svg>
        </span>
        <input type="text" placeholder="Username" class="w-full pl-12 pr-4 py-3 border-b-2 border-gray-300 focus:outline-none focus:border-blue-400 rounded-md font-medium text-gray-700" bind:value={username}/>
      </div>

      <!-- Password -->
      <div class="relative">
        <span class="absolute left-3 top-3 text-blue-500">
          <!-- Heroicons lock icon -->
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2a5 5 0 00-5 5v4h-1a1 1 0 00-1 1v10a1 1 0 001 1h12a1 1 0 001-1V12a1 1 0 00-1-1h-1V7a5 5 0 00-5-5zM9 7a3 3 0 116 0v4H9V7z"/></svg>
        </span>
        <input type="password" placeholder="Password" class="w-full pl-12 pr-4 py-3 border-b-2 border-gray-300 focus:outline-none focus:border-blue-400 rounded-md font-medium text-gray-700" bind:value={password}/>
      </div>

      <button class="w-full py-3 bg-blue-500 text-white font-semibold rounded-2xl hover:bg-blue-600 transition duration-200" onclick={handleSignin}>
        Sign in
      </button>

      <p class="text-gray-500 text-center">
        Don't have an account? <a href="/register" class="text-blue-600 font-semibold hover:underline">Register</a>
      </p>
    </div>
  </section>
</main>
