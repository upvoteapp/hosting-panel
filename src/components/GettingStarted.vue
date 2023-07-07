<template>
  <div class="gettingstarted">
    <br />
    <h1 class="poppins-head">Getting Started with Kosciuszko 2.0</h1>
    <br />

    <h1 class="text-xl text-center">To begin, edit <code class=" bg-slate-900 rounded-md"> /src/views/HomeView.vue </code></h1>
    <br />
    <h1 class="text-xl text-center">Remember, you can prevent this page from showing by just changing the environment variable <br /> <code class=" bg-slate-900 rounded-md"> VITE_FRONTPAGE_ENABLED = 'true'</code> to <code class=" bg-slate-900 rounded-md"> VITE_FRONTPAGE_ENABLED = 'false'</code> in .env</h1> <br/>
    <br />
    <div class="flex flex-col justify-center items-center">
      <a href="https://kosciuszko.aviance.app" class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded"> Click me to view documentation</a>
    </div>
    <br />
    <br />
  </div>
</template>

<style scoped>
.poppins-head {
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  font-size: 2.5rem;
  color: white;
  text-align: center;
}
.gettingstarted {
  color: white;
  background-color: #1e1e1e;
}

.nge {
  background-color: #1e1e1e;
}
</style>