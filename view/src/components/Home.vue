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
          <button class="cta-button">登录</button>
        </div>
        <div class="register-box cta-box">
          <button class="cta-button">注册</button>
        </div>
      </div>
    </main>
    <!-- Footer -->
    <footer>
      <p class="about">关于</p>
    </footer>
  </div>
</template>
  
<script>
  export default {
    name: 'Home',
    // Your component logic goes here
  };
</script>
  
<style scoped>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
}

.homepage {
  background-color: #F5F5DC;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  position: relative; /* 添加相对定位 */
}

header {
  text-align: center;
}

.logo {
  font-size: 32px;
  margin-bottom: 5px;
  position: absolute;
  top: 25px;
  left: 50%; /* 使用left和transform属性进行水平居中对齐 */
  transform: translateX(-50%);
}

.slogan {
  font-size: 100px;
  color: #000;
  font-family: 'Your Desired Font', sans-serif;
  font-weight: bold; /* 添加这一行来设置为粗体 */
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
  flex-direction: column; /* 修改为垂直排列 */
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

.register-box .cta-button {
  color: #000; /* 设置文字颜色为黑色 */
}

.login-box {
  background-color: #000;
  color: #fff;
  border-radius: 15px; /* 设置圆角半径 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-box {
  background-color: #fff;
  color: #000;
  border-radius: 15px; /* 设置圆角半径 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.cta-button {
  width: 500px;
  height: 60px;
  padding: 10px;
  font-size: 16px;
  color: #fff; /* 设置文字颜色为白色 */
  background-color: transparent; /* 设置背景色为透明 */
  border: none; /* 移除按钮边框 */
  cursor: pointer; /* 添加鼠标指针效果 */
}

.footer {
  position: fixed;
  bottom: 20px;
  width: 100%;
  text-align: center;
  padding: 20px; /* 可选，根据需要调整 */
  background-color: #F5F5DC; /* 与页面背景颜色一致 */
}
.about {
  font-size: 16px;
  color: #000; /* 设置文字颜色为黑色 */
  cursor: pointer;
}

</style>
