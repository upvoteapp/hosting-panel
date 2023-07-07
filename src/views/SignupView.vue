<template>
    <div class="gradient">
    <div class="signup">
    </div>
    <div class="signup-middle-center">
        <div class="darkmode">
          <h1 class="text-4xl font-bold text-center">Kosciuszko 2.0</h1>
          <br />
          <p class="text-lg text-center">Welcome to Kosciuszko 2.0, please create an account to access the Dashboard.</p>
          <form action="" method="POST">
            <div class="mt-4">
              <label class="block text-white text-sm font-bold mb-2" for="username">
                Username:
              </label>
              <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" required placeholder="Username">
            </div>
            <div class="mt-4">
              <label class="block text-white text-sm font-bold mb-2" for="password">
                Email:
              </label>
              <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="text" required placeholder="Email">
            </div>
            <div class="mt-4">
              <label class="block text-white text-sm font-bold mb-2" for="password">
                Password:
              </label>
              <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" required placeholder="Password">
            </div>
            <div class="mt-4 flex flex-col items-center">
              <button type="submit" class="bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                Signup
              </button>
            </div>
            <div class="mt-4">
              <p class="text-sm text-center text-white">Already have an account? <a href="/login" class="underline"><strong> Login </strong></a></p>
            </div>
          </form>
        </div>
      </div>
    </div>
</template>
  
<style scoped>
    .gradient {
      background: linear-gradient(to bottom right, #2d09e1, #a00505);
    }
    input {
      background-color: #2f2f2f;
      color: white;
    }
    .signup {
      /* background: linear-gradient(to bottom right, #2d09e1, #a00505); */
      background-repeat: no-repeat;
      background-size: cover;
      background-image: url(/signup_screen.png);
      background-position: center;
      color: white;
      height: 100vh;
      filter: blur(1.5px)
    }

    .signup-middle-center {
      position: absolute;
      color: white;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    .darkmode {
      background-color: #2f2f2f;
      padding: 20px;
      opacity: 0.85;
      width: 350px;
      border-radius: 10px;
    }
    input:-webkit-autofill {
      -webkit-box-shadow:200px 200px 100px #2f2f2f inset; 
      box-shadow:200px 200px 100px #2f2f2f inset; 
    }
</style>