<template>
    <div class="login">
    </div>
    <div class="login-middle-center">
        <div class="darkmode">
          <h1 class="text-4xl font-bold text-center">Kosciuszko 2.0</h1>
          <br />
          <p class="text-lg text-center">Welcome back! Please enter your login information to continue.</p>
          <form action="" method="POST">
            <div class="mt-4">
              <label class="block text-white text-sm font-bold mb-2" for="username">
                Username:
              </label>
              <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username">
            </div>
            <div class="mt-4">
              <label class="block text-white text-sm font-bold mb-2" for="password">
                Password:
              </label>
              <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Password">
            </div>
            <div class="mt-4 flex flex-col items-center">
              <button type="submit" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                Login
              </button>
            </div>
            <div class="mt-4">
              <p class="text-sm text-center text-white">Don't have an account? <a href="/signup" class="underline"><strong> Sign Up </strong></a></p>
            </div>
          </form>
        </div>
      </div>

 </template>
  
<style scoped>
    input {
      background-color: #2f2f2f;
      color: white;
    }
    .login {
      background-image: url(/login_screen.png);
      background-repeat: no-repeat;
      background-size: cover;
      background-position: center;
      color: white;
      height: 100vh;
      filter: blur(0.5px)
    }

    .login-middle-center {
      position: absolute;
      color: white;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    input:-webkit-autofill {
      color: white;
      -webkit-box-shadow:200px 200px 100px #2f2f2f inset; 
      box-shadow:200px 200px 100px #2f2f2f inset; 
    }
    .darkmode {
      background-color: #2f2f2f;
      padding: 20px;
      opacity: 0.85;
      width: 350px;    
      border-radius: 10px;
    }
</style>