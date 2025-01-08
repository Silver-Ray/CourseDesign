<script setup>
import eachProgrammer from './eachProgrammer.vue'
</script>

<template>
  <div class="wholeProgrammer">
    <eachProgrammer :name="'王玺之'" :percentage="33" :email="'1678743449@qq.com'"/>
    <eachProgrammer :name="'王玺之'" :percentage="33" :email="'1678743449@qq.com'"/>
    <eachProgrammer :name="'王玺之'" :percentage="33" :email="'1678743449@qq.com'"/>
  </div>
</template>

<script>
export default {
  name: 'showProgrammer',

}
</script>

<style scoped>
/* 清除默认样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
li {
  list-style: none;
}
a {
  color: #333;
  text-decoration: none;
}

/* 整个区域规格 */
.wholeProgrammer{
  display: flex;
  height: 100vh;
  width: 100%;
}
</style>