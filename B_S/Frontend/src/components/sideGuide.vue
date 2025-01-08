<template>
  <div id="sideguide">
    <ul>
      <li><router-link to="/" :class=activeStateH @click.prevent="Home">首页</router-link></li>
      <li><router-link to="/programmer" :class=activeStateP @click.prevent="Programmer">小组成员</router-link></li>
    </ul>
  </div>
</template>

<script>

export default{
  name: 'sideGuide',
  props: {
    activeState: {
      type: Number,
      default: 0
    }
  },
  data(){
    return{
      active: 'Home',
      activeStateH: this.activeState === 0 ? 'nowActive' : 'nowInactive',
      activeStateP: this.activeState === 1 ? 'nowActive' : 'nowInactive',
    }
  },
  methods:{
    Home(){
      this.active = 'Home';
      this.$emit('data-update', this.active);
    },
    Programmer(){
      this.active = 'Programmer';
      this.$emit('data-update', this.active);
    }
  }
};
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

/* 定义侧导航栏的规格 */
#sideguide {
  height: 600px;
  background-color: #202b3e;
}
#sideguide a{
  display: block;
  padding-left: 30px;
  height: 80px;
  line-height: 80px;
  font-size: 20px;
  color: #fff;
  transition: transform 0.5s ease, background-color 0.5s ease;
}
#sideguide a:hover{
  transform: scale(1.3);
  background-color: #3c4c68;
}
#sideguide .nowInactive{
  border-bottom: 3px solid #c7c7c7;
}
#sideguide .nowActive{
  border-bottom: 6px solid #6f9fff;
}
</style>