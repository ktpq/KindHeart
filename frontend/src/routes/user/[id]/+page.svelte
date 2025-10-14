<script>
    export let data;
    import UserEvent from "./UserEvent.svelte";

    let user = data.user;
    let events = data.events;
</script>

<main class="p-5">

    <!-- Header -->
    <section class="flex items-center space-x-5">
        <a class="cursor-pointer" href="/admin">
            <!-- Arrow Left SVG -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-blue-600 hover:text-blue-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
        </a>
        <!-- Bell SVG -->
        <!-- <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C8.67 6.165 8 7.388 8 8.75v5.408c0 .536-.21 1.05-.586 1.414L6 17h5m4 0v1a3 3 0 11-6 0v-1h6z"/>
        </svg> -->
        <h1 class="text-3xl text-blue-700 font-semibold">User Profile</h1>
    </section>

    <!-- Profile Section -->
    <section class="mt-10 w-[65%] mx-auto p-7 flex flex-col items-center space-y-4 bg-white rounded-2xl shadow-md">
        <img src="/profile/handsome.jpg" alt="" width="125" class="rounded-full border-4 border-blue-300">
        <p class="text-2xl font-bold text-blue-800">{user.username}</p>
        <div class="flex items-center space-x-3">
            <!-- Email SVG -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16 12h.01M12 16h.01M8 12h.01M21 12c0 4.418-4.03 8-9 8s-9-3.582-9-8 4.03-8 9-8 9 3.582 9 8z"/>
            </svg>
            <p class="text-lg font-medium text-blue-700">{user.email}</p>
        </div>
    </section>

    <!-- Events Header -->
    <section class="flex items-center space-x-5 mt-7">
        <!-- Bell SVG -->
        <!-- <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C8.67 6.165 8 7.388 8 8.75v5.408c0 .536-.21 1.05-.586 1.414L6 17h5m4 0v1a3 3 0 11-6 0v-1h6z"/>
        </svg> -->
        <h1 class="text-4xl text-blue-700 font-bold mt-7">Events Created</h1>
    </section>

    <!-- Events Section -->
    <section class="mt-7">
        {#each events as event, i}
            <UserEvent event={event}/>
        {/each}
    </section>

</main>
