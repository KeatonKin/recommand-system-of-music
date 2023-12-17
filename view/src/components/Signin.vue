<template>
  <div class="login-page" ref="loginPageRef">
    <div class="photo">
      <img src="/logo/nobody.png" alt="DinoFm photo" />
    </div>
    <h2 class="signin-heading">Sign in to DinoFm</h2>
    <input type="text" placeholder="用户名" class="input-field" />
    <input type="password" placeholder="密码" class="input-field" />
    <button class="signin-button">登录</button>
    <p class="signup-link">没有账号? <router-link to="/signup">去注册</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'Signin',
  mounted() {
    document.title = 'DinoFm';
  },
};
</script>

<style scoped>
.login-page {
  background-color: #F5F5DC;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 93vh;
}

.photo {
  margin-bottom: 10px; /* 适当的边距 */
}

.photo img {
  width: 200px; /* 调整 Logo 的宽度 */
  height: 200px; /* 调整 Logo 的高度 */
}

.signin-heading {
  font-size: 24px;
  margin-bottom: 20px;
}

.input-field {
  width: 250px;
  height: 25px;
  margin-bottom: 10px;
  padding: 5px;
  border-radius: 6px;
  font-size: 16px;
  border: 2px solid #ccc; /* 添加边框样式 */
  transition: border-color 0.3s; /* 添加过渡效果 */

  /* 输入框选中后的样式 */
  &:focus {
    outline: none; 
    border: 2px solid #1aca20;
  }
}

.signin-button {
  width: 100px;
  height: 25px;
  font-size: 16px;
  color: #fff;
  background-color: #000;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.register-link {
  margin-top: 20px;
  font-size: 14px;
  color: #000;
}
</style>
