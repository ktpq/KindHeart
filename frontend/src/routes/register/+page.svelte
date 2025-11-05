<script>
  import { goto } from "$app/navigation";
  import axios from "axios";
  import Swal from "sweetalert2";

  let username = $state()
  let email = $state()
  let password = $state()
  let confirmPassword = $state()

  const handleRegister = async () => {
    try{
      const base_api = import.meta.env.VITE_API_URL
      if (password !== confirmPassword){
        Swal.fire({
          icon: 'error',
          title: 'รหัสผ่านไม่ตรงกัน',
          confirmButtonColor: '#3B82F6'
        })
        return
      }
      await axios.post(`${base_api}/api/auth/register/`, {username, email, password})
      Swal.fire({
        icon: 'success',
        title: 'ลงทะเบียนสำเร็จ!',
        confirmButtonColor: '#3B82F6'
      }).then(() => goto('/login'))
    } catch (error){
      console.log(error.response.data)
      Swal.fire({
        icon: 'error',
        title: 'ไม่สามารถลงทะเบียนได้',
        text: 'username อาจซ้ำ',
        confirmButtonColor: '#3B82F6'
      })
    }
  }
</script>

<main class="bg-gray-50 h-screen flex justify-center items-center px-4">
  <section class="w-full max-w-md bg-white rounded-3xl shadow-2xl px-10 py-12" data-aos="fade-up" data-aos-duration="1500">
    <h1 class="text-4xl font-bold mb-8 text-center text-gray-800">Register</h1>

    <div class="space-y-6">
      <!-- Username -->
      <div class="relative">
        <span class="absolute left-3 top-3 text-blue-500">
          <!-- Heroicons user icon -->
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.667 0 8 1.333 8 4v2H4v-2c0-2.667 5.333-4 8-4zm0-10a4 4 0 100 8 4 4 0 000-8z"/></svg>
        </span>
        <input type="text" placeholder="Username" class="w-full pl-12 pr-4 py-3 border-b-2 border-gray-300 focus:outline-none focus:border-blue-400 rounded-md font-medium text-gray-700" bind:value={username}/>
      </div>

      <!-- Email -->
      <div class="relative">
        <span class="absolute left-3 top-3 text-blue-500">
          <!-- Heroicons mail icon -->
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M2 4h20v16H2V4zm2 2v2l8 5 8-5V6H4zm0 4v8h16v-8l-8 5-8-5z"/></svg>
        </span>
        <input type="text" placeholder="Email" class="w-full pl-12 pr-4 py-3 border-b-2 border-gray-300 focus:outline-none focus:border-blue-400 rounded-md font-medium text-gray-700" bind:value={email}/>
      </div>

      <!-- Password -->
      <div class="relative">
        <span class="absolute left-3 top-3 text-blue-500">
          <!-- Heroicons lock icon -->
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2a5 5 0 00-5 5v4h-1a1 1 0 00-1 1v10a1 1 0 001 1h12a1 1 0 001-1V12a1 1 0 00-1-1h-1V7a5 5 0 00-5-5zM9 7a3 3 0 116 0v4H9V7z"/></svg>
        </span>
        <input type="password" placeholder="Password" class="w-full pl-12 pr-4 py-3 border-b-2 border-gray-300 focus:outline-none focus:border-blue-400 rounded-md font-medium text-gray-700" bind:value={password}/>
      </div>

      <!-- Confirm Password -->
      <div class="relative">
        <span class="absolute left-3 top-3 text-blue-500">
          <!-- Heroicons lock icon -->
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2a5 5 0 00-5 5v4h-1a1 1 0 00-1 1v10a1 1 0 001 1h12a1 1 0 001-1V12a1 1 0 00-1-1h-1V7a5 5 0 00-5-5zM9 7a3 3 0 116 0v4H9V7z"/></svg>
        </span>
        <input type="password" placeholder="Confirm Password" class="w-full pl-12 pr-4 py-3 border-b-2 border-gray-300 focus:outline-none focus:border-blue-400 rounded-md font-medium text-gray-700" bind:value={confirmPassword}/>
      </div>

      <button class="w-full py-3 bg-blue-500 text-white font-semibold rounded-2xl hover:bg-blue-600 transition duration-200" onclick={handleRegister}>
        Sign up
      </button>

      <p class="text-gray-500 text-center">
        Already have an account? <a href="/login" class="text-blue-600 font-semibold hover:underline">Login</a>
      </p>
    </div>
  </section>
</main>
