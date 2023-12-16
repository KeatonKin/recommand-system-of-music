<script setup>


  const click = ()=>{


   fetch("/api/api/get_name")
  .then((response) => response.json())
  .then((data) => console.log(data));

  }
</script>

<template>
  <button @click="click">111</button>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
