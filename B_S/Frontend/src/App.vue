<script setup>
  import Home from './Home.vue'
  import Programmer from './Programmer.vue';
</script>

<template>
    <div>
      <Home @data-update1H="handleChangeHome" v-if="active=='Home'"/>
    </div>
    <div>
      <Programmer @data-update1P="handleChangeProgrammer" v-if="active=='Programmer'"/>
    </div>
</template>

<script>
export default {
  data(){
    return {
      active: 'Home'
    }
  },
  methods: {
    handleChangeHome(data) {
      this.active = data;
    },
    handleChangeProgrammer(data) {
      this.active = data;
    }
  }
};
</script>

<style scoped>
body {
  font: 14px/1.5 "Microsoft Yahei", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  color: #333;
  background-color: #f3f5f7;
  background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.5)), url('./assets/背景图.png');
  background-attachment: fixed;
}

/* 主功能窗口 */
.mainWindow {
  display: flex;
}

/* 左侧 */
.mainWindow .left{
  display: flex;
  flex-direction: column;

  width: 150px;
  height: 90vh;
}

/* 右侧 */
.mainwindow .right{
  flex: 1;
  /* background-color: #ff8181; */
}

</style>

