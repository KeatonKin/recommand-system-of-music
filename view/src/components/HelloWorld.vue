<template>
  <div class="homepage">
    <!-- Header -->
    <header>
      <h1 class="logo">DinoFM</h1>
      <p class="slogan">Listen Now</p>
    </header>

    <!-- Main content area -->
    <main>
      <div class="cta">
        <!-- Call-to-action buttons (e.g., Register and Login) -->
        <button class="cta-button">Register</button>
        <button class="cta-button">Login</button>
      </div>
    </main>

    <!-- Footer -->
    <footer>
      <p class="about">About</p>
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
/* Your component styles go here */
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
}

.homepage {
  background-color: #FFDAB9;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

header {
  text-align: center;
}

.logo {
  font-size: 20px;
  margin-bottom: 10px;
}

.slogan {
  font-size: 50px;
}

main {
  margin-top: 20px;
}

.cta {
  display: flex;
  gap: 10px;
}

.cta-button {
  padding: 10px;
  font-size: 16px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  cursor: pointer;
}

footer {
  margin-top: 20px;
}

.about {
  font-size: 16px;
  cursor: pointer;
}
</style>
