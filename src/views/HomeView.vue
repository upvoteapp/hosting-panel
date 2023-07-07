<script setup lang="ts">
import GettingStarted from '../components/GettingStarted.vue'
</script>

<template>
  <!-- <nav class="navbar navbar-expand-lg bg-gray-900">
    <div class="container-fluid">
      <a class="navbar-brand textpad2" href="#">Kosciuszko 2.0 by avnce.</a>
    </div>
  </nav> -->
  <div class="home">
    <div class="brand">
      <div class="container">
        <div class="row">
          <div class="col-12 text-pad">
            <br />
            <h3 class="noto-sans-jp lg:text-xl md:text-xl text-left sm:text-lg">ホスティングをより良くする</h3>
            <br />
            <!-- Make small for small screens -->
            <h1 class="text-left navbar-brand lg:text-8xl flex-wrap sm:text-4xl whitespace-break-spaces">Supercharge your hosting experience with Upvote.</h1>
            <br />
            <br />
            <h1 class="navbar-brand lg:text-2xl md:text-xl"> A simple but Powerful Panel designed <span class="underline">for all your hosting needs.</span></h1>
            <br />
            <br />
          </div>
        </div>
      </div>
    </div>
    <div>
      <!-- Make rounded card in tailwindcss and fit width -->
      <div class="bg-gray-900 rounded-lg text-white text-center p-10">
        <h1> <font-awesome-icon :icon="['fas', 'check-circle']" size="lg" style="color: #00e639;"/> <span style="font-size: large;">You own this panel, plus, we don't have BS unlike Hye Ararat.</span></h1>
      </div>
    </div>
    <div>
      <GettingStarted/>

    </div>
  </div>
</template>

<style scoped>
 @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@700&display=swap');
  .home {
    background-color: #1e1e1e;
    color: white;
    height: 100vh;
  }
  .brand {
    /* Make the background Color a gradient */
    background-image: linear-gradient(to right, #5917c2, #550560);
    color: white;
  }
  .navbar-brand {
    color: white;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
  }
  .noto-sans-jp {
    font-family: 'Noto Sans JP', sans-serif;
  }

  .text-pad {
    padding-left: 5%;
    padding-right: 20%;
  }
  .textpad2 {
    padding-left: 1.25%;
  }
</style>