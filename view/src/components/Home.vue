<template>
  <div class="homepage">
    <!-- Header -->
    <header>
      <h1 class="logo">D/NOFM</h1>
      <p class="slogan">Let's Listen Now</p>
    </header>
    <!-- Main content area -->
    <main>
      <div class="cta">
        <div class="login-box cta-box">
          <router-link to="/signin" class="cta-button">登录</router-link>
        </div>
        <div class="register-box cta-box">
          <router-link to="/signup" class="cta-button">注册</router-link>
        </div>
      </div>
    </main>
    <!-- Footer -->
    <footer class="footer">
      <router-link to="/about" class="about">关于</router-link>
    </footer>
  </div>
</template>
  
<script>
  export default {
    name: 'Home',
    mounted() {
      document.title = 'DinoFm';
    },
    
    // Your component logic goes here
  };
</script>
  
<style scoped>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
}

.homepage {
  background: linear-gradient(to right, #F5F5DC, #F5DEB3);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  position: relative; 
}

header {
  text-align: center;
}

.logo {
  font-size: 32px;
  margin-bottom: 5px;
  position: absolute;
  top: 25px;
  left: 50%; 
  transform: translateX(-50%);
}

.slogan {
  font-size: 100px;
  color: #000;
  font-family: 'Your Desired Font', sans-serif;
  font-weight: bold; 
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

main {
  margin-top: 20px;
}

.cta {
  display: flex;
  flex-direction: column; 
  gap: 10px;
}

.login-box,
.register-box {
  width: 576px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box .cta-button {
  color: #fff;
  text-decoration: none; /* 去掉下划线 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-box .cta-button {
  color: #000;
  text-decoration: none;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box:hover .cta-button {
  text-decoration: none; /* 去掉下划线 */
}

.register-box:hover .cta {
  text-decoration: none;
}

.login-box {
  background-color: #000;
  color: #fff;
  border-radius: 15px; 
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-box {
  background-color: #fff;
  color: #000;
  border-radius: 15px; 
  display: flex;
  justify-content: center;
  align-items: center;
}

.cta-button {
  width: 500px;
  height: 60px;
  padding: 10px;
  font-size: 16px;
  color: #fff; 
  background-color: transparent; 
  border: none; 
  cursor: pointer; 
}

.footer {
  position: fixed;
  bottom: 10px;
  width: 100%;
  text-align: center;
  padding: 20px; 
  background: linear-gradient(to right, #F5F5DC, #F5DEB3);
}
.about {
  font-size: 16px;
  color: #000; 
  cursor: pointer;
  text-decoration: underline;
}

</style>
