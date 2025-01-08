<template>
  <div id="searcharea">
    <input class="inputtext" type="text" v-model="url" placeholder='请输入要爬取的URL' @keydown.enter="postURL(url)">
    <a href="#" @click.prevent="postURL(url)"></a>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'urlSearch',
  data() {
    return {
      url: '',
    }
  },
  methods: {
    delay(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    async postURL(url) {
      console.log(url);
      try {
        this.$emit('isRunningNewFile');
        const response1 = await axios.post('http://localhost:8000/api/postURL/', {URL: url});
        await this.delay(1000);
        this.$emit('isFinishedNewFile');
        console.log("Spide finished.");

        const response2 = await axios.get('http://localhost:8000/api/isAnalyzeFinished/');
        this.$emit('isFinishedAnalyze', response2.data);
        console.log(response2.data);
        console.log("Analyze finished.");
      }
      catch(error) {
        console.error('Error:', error);
      }
    }
  }
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

/* 定义整个搜索栏的规格 */
#searcharea {
  display: flex;
  margin: 20px auto;
  padding-left: 20px;
  padding-right: 18px;
  width: 800px;
  height: 60px;
  /* background-color: #ededed; */
  background-color: #fff;
  border: 1px solid #000;
  border-radius: 30px;
}
/* 输入栏样式 */
#searcharea input {
  flex: 1;
  border: 0;
  background-color: transparent;
  /* 去掉焦点框 */
  outline: none;
}
/* 选中placeholder属性 */
#searcharea input::placeholder {
  font-size: 18px;
  color: #999;
}
#searcharea .inputtext {
  font-size: 18px;
}
#searcharea a {
  align-self: center;

  width: 20px;
  height: 20px;
  background-image: url(../assets/搜索.png);
  background-size: contain;
  background-repeat: no-repeat;
}

#searcharea:focus-within {
  background-color: #e5f8f8; /* 获取焦点时的背景颜色 */
}
</style>