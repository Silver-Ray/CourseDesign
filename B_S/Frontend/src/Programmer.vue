<script setup>
import textInput from './components/textInput.vue'
import sideGuide from './components/sideGuide.vue'
import showProgrammer from './components/showProgrammer.vue'
</script>

<template>
  <body class="mainWindow">
    <div class="left">
      <sideGuide @data-update="handleChange" :activeState="1"/>
    </div>

    <div class="right">
      <div>
        <showProgrammer/>
      </div>
    </div>
  </body>
</template>

<script>
export default {
  name: 'Programmer',
  methods: {
    handleChange(data){
      this.$emit('data-update1P', data);
    }
  }
};
</script>

<style scoped>
body {
  font: 14px/1.5 "Microsoft Yahei", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  color: #333;
  background-color: #f3f5f7;
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
  height: 600px;
}

/* 右侧 */
.mainWindow .right{
  flex: 1;
  display: flex; /* 添加flex布局 */
  flex-direction: column; /* 垂直排列子元素 */
  align-items: center; /* 水平居中 */
  margin: 0 auto; /* 水平居中整个.right容器 */
}

</style>

