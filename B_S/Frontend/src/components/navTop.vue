<template>
  <nav class="navbar">
    <ul>
      <li><a href="#sec1" @click.prevent="scrollToSection('sec1')">上传区域</a></li>
      <li><a href="#sec2" @click.prevent="scrollToSection('sec2')">热评</a></li>
      <li><a href="#sec3" @click.prevent="scrollToSection('sec3')">情绪分析</a></li>
      <!-- <li><a href="#sec4" @click.prevent="scrollToSection('section4')">联系我们</a></li> -->
    </ul>
  </nav>
</template>

<script>
export default {
  methods: {
    scrollToSection(id) {
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
}
</script>

<style scoped>
.navbar {
  width: 100%;
  background-color: #333;
  color: white;
  padding: 15px 100px;
  padding-top: 20px;
  text-align: center;
}
.navbar ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  justify-content: space-between;
}
.navbar a {
  color: white;
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
}
.navbar a:hover {
  color: coral;
}
</style>