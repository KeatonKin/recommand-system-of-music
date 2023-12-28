<template>
  <div class="register-page" ref="signupPageRef">
    <h2 class="signup-heading">Sign up to DinoFm</h2>
    <input type="text" placeholder="用户名" class="input-field" v-model="username" id="username" required/>
    <input type="password" placeholder="密码" class="input-field" v-model="password" id="password" required/>
    <input type="password" placeholder="确认密码" class="input-field" v-model="password" id="cf-password" required/>
    <button class="signup-button" @click="signup">注册</button>
    <p class="signin-link">已有账号? <router-link to="/signin">去登录</router-link></p>
  </div> 
</template>
  
<script>
  export default {
    
  };
</script>
  
<style scoped>
.register-page {
  background: linear-gradient(to right, #F5F5DC, #F5DEB3);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 93vh;
}

.signup-heading {
  font-size: 35px;
  margin-bottom: 20px;
}

.input-field {
  width: 360px;
  height: 25px;
  margin-bottom: 10px;
  padding: 5px;
  border-radius: 6px;
  font-size: 16px;
  border: 2px solid #ccc;
  transition: border-color 0.3s;

  &:focus {
    outline: none;
    border: 2px solid #1aca20;
  }
}

.signup-button {
  width: 100px;
  height: 25px;
  font-size: 16px;
  color: #fff;
  background-color: #FF6A6A;
  border: none;
  cursor: pointer;
  border-radius: 5px;

  &:hover {
    background-color: #EE6363;
  }
}

.signin-link {
  margin-top: 20px;
  font-size: 14px;
  color: #000;
}

</style>
  