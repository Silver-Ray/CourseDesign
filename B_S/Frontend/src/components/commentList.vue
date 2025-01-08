<template>
  <div :class="{loading: isSpiding}">
    <div v-if="isSpiding" class="loadingText">加载中...</div>
    <div v-else>
      <div class="mainblog">
        <div class="title">博文</div>
        <div class="maincontent">
          <h2>发布者：{{ name }}</h2>
          <div class="cont">{{ content }}</div>
          <p>点赞数：{{ likes }} | 评论数：{{ comment_num }} | 转发数：{{ repost_num }} </p>
        </div>
      </div>
      <ul class="commentColumn">
        <p>评论区</p>
        <li v-for="({time, name, comment, place}) in comments">
          <div class="commentator">
            <span class="name">{{ name }} : </span>
            <span class="time">{{ time }}</span>
            <span class="place">{{ place }}</span>
          </div>
          <div>{{ comment }}</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import Papa from 'papaparse';
import moment from 'moment-timezone';
import {watch} from 'vue';
import axios from 'axios';

export default {
  name: 'commentList',
  data() {
    return {
      comments : [],
      content: '2啊沙发沙发沙发沙发去问问服务绿湾i理论',
      likes: '111',
      comment_num: '2321',
      repost_num: '1124',
      name: '红星新闻'
    }
  },
  props: {
    fileState: {//上传文件时变化
      type: Boolean,
      required: true
    },
    isSpiding: {//开始爬取时置true
      type: Boolean,
      required: true,
    }
  },
  methods: {
    async loadCSV() {
      try {
        const response = await axios.get('http://localhost:8000/api/commentList/');
        const csvText = response.data;
        const results = Papa.parse(csvText, { header: true });
        this.comments = results.data.map(row => {
          let time = row.created_at;
          try {
            // 根据CSV文件中的时间格式调整moment的format参数
            const date = moment(time, 'YYYY/MM/DD HH:mm');
            time = date.format('YYYY-MM-DD dddd'); // 格式化日期为 "YYYY-MM-DD dddd"
          } catch (error) {
            console.error('Invalid date:', row.created_at);
          }
          return {
            time: time,
            comment: row.text_raw,
            place: row.source || 'Unknown', // 如果source为空，则显示'Unknown'
            name: row.name
          };
        });
        if (this.comments.length > 0) {
          this.comments.pop();
        }
      }
      catch(error) {
        console.error(error);
        return null;
      }
    }
  },
  mounted() {
    this.loadCSV(); // 在组件挂载时调用loadCSV方法
  },
  watch: {
    fileState: {
      handler() {
        this.loadCSV();
      },
      immediate: true // 立即执行handler函数
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

.mainblog {
  display: flex; /* 使用 flexbox 布局 */
  flex-direction: column; /* 设置为垂直方向 */
  justify-content: space-between; /* 在标题和内容之间分配空间 */
  background-color: #fdc2c2;
  border: 2px solid #000;
  border-bottom: 0;
  border-top-left-radius: 9px;
  border-top-right-radius: 9px;
  box-sizing: border-box; /* 确保内边距和边框包含在容器的总宽度和高度内 */
}
.mainblog .title {
  font-size: 25px;
  padding: 5px 0;
  font-weight: bold;
  color: #000;
  text-align: center;
}
.mainblog h2 {
  font-size: 25px;
  font-weight: bold;
}
.mainblog .maincontent {
  display: flex; /* 使用 flexbox 布局 */
  flex-direction: column; /* 设置为垂直方向 */
  justify-content: flex-end; /* 将内容对齐到容器的底部 */
  background-color: #fff;
  border-radius: 9px;
  padding: 5px 20px;
  min-height: 300px; /* 设置最小高度 */
  font-size: 18px;
  /* font-size: 80px; */
}
.mainblog .maincontent p {
  margin: 0; /* 移除 p 标签的默认外边距 */
  text-align: center; /* 将文本居中对齐 */
  margin-top: auto; /* 将 p 标签推到容器的底部 */
  font-size: 16px;
}

/* 列表栏的大小规格 */
.commentColumn {
  width: 804px;
  height: 604px;
  padding-right: 2px;
  overflow-y: auto;
  background-color: #fdc2c2;
  border: 2px solid #000;
  border-top: 0;
  border-bottom-right-radius: 9px;
  border-bottom-left-radius: 9px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

/* 滚动条的伪元素 */
::-webkit-scrollbar {
  width: 8px; /* 可以设置滚动条的宽度 */
}
::-webkit-scrollbar-thumb {
  background-color: #b0b0b0;
  margin: 100px;
  border-radius: 4px; /* 可以为滚动条滑块添加圆角 */
}
::-webkit-scrollbar-track {
  background-color: #e7e7e7;
  border-radius: 4px; /* 可以为滚动条轨道添加圆角 */
}
/* 评论条样式 */
.commentColumn p {
  font-size: 25px;
  font-weight: bold;
  color: #000;
  text-align: center;
  margin: 5px;
}
.commentColumn .commentator{
  line-height: 25px;
  border-bottom: 1px solid #000;
  color: #999;
}
.commentColumn .commentator .name{
  font-weight: bold;
  font-size: 18px;
  color: #000;
}
.commentColumn .commentator .time{
  font-size: 14px;
}
.commentColumn .commentator .place{
  font-size: 14px;
  float: right;
}

.commentColumn li {
  margin: 3px 2px;
  font-size: 16px;
  padding: 5px 10px 10px;
  line-height: 18px;
  border-radius: 27px;
  border: 1px solid #000;
  word-wrap: break-word; /* 允许在单词内换行 */
  overflow-wrap: break-word; /* 同上，为了更好的兼容性 */
  background-color: #fbfbfb;
}

.loading {
  background-color: #fff;
  width: 804px;
  height: 604px;
  border: 3px solid #000;
  border-radius: 9px;
  text-align: center;
}
.loadingText {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 20px;
  font-weight: bold;
  color: #000;
}
</style>