<template>
  <div>
    <a-float-button-group
      shape="circle"
      style="inset-inline-end: 24px;"
    >
      <!-- 第一个悬浮按钮，带有文本"sec1"和悬浮气泡 -->
      <a-popover content="转到上传区域" trigger="hover" placement="left">
        <a-float-button @click="scrollToSection('sec1')">
          <template #icon>
            <div>s1</div>
          </template>
        </a-float-button>
      </a-popover>
      <!-- 第二个悬浮按钮，带有文本"sec2"和悬浮气泡 -->
      <a-popover content="转到热评" trigger="hover" placement="left">
        <a-float-button @click="scrollToSection('sec2')">
          <template #icon>
            <div>s2</div>
          </template>
        </a-float-button>
      </a-popover>
      <!-- 第三个悬浮按钮，带有文本"sec3"和悬浮气泡 -->
      <a-popover content="转到情绪分析" trigger="hover" placement="left">
        <a-float-button @click="scrollToSection('sec3')">
          <template #icon>
            <div>s3</div>
          </template>
        </a-float-button>
      </a-popover>
      <!-- 第四个悬浮按钮，带有悬浮气泡，内容是“回到顶部” -->
      <a-popover content="回到顶部" trigger="hover" placement="left">
        <a-float-button-back-top :visibility-height="0" />
      </a-popover>
    </a-float-button-group>
  </div>
</template>

<script>
import { FloatButton, FloatButtonGroup, Popover } from 'ant-design-vue';

export default {
  components: {
    'a-float-button': FloatButton,
    'a-float-button-group': FloatButtonGroup,
    'a-popover': Popover,
    'a-float-button-back-top': FloatButton.BackTop
  },
  methods: {
    scrollToSection(id) {
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
};
</script>

<style scoped>
/* 在这里添加组件的样式 */
</style>