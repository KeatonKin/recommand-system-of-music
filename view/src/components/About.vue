<template>
  <div class="about-page" ref="aboutPageRef">
    <div class="about-content">
      <h2>About Me</h2>
      <p>Welcome to my about page.</p>
      <p>Here you can learn more about who I am and what I do.</p>
      <p>旨在设计一个音乐推荐系统</p>
      <p>Github主页</p>
      <a href="https://github.com/KeatonKin" class="goGithub">点击前往</a>
      <p> </p>
    </div>
    <router-link to="/" class="back-button">
      <i class="fas fa-arrow-left"></i> 返回主页
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'About',
  mounted() {
    document.title = 'DinoFm';
  },
};
</script>

<style scoped>

.about-page {
  background: linear-gradient(to right, #F5F5DC, #F5DEB3);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 93vh;
}

.back-button {
  font-size: 18px;
  color: #333;
  text-decoration: none;
  margin-bottom: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.back-button i {
  margin-right: 5px;
}

.about-content {
  max-width: 800px;
  text-align: center;
}

.goGithub {
  color: #666;
  font-size: 18px;
}

h2 {
  font-size: 36px;
  color: #333;
}

p {
  font-size: 18px;
  color: #666;
  line-height: 1.6;
}
</style>
