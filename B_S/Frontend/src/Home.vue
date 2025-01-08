<script setup>
import textInput from './components/textInput.vue'
import urlInput from './components/urlInput.vue'
import sideGuide from './components/sideGuide.vue'
import commentList from './components/commentList.vue'
import barChart from './components/barChart.vue'
import barChartC from './components/barChartcopy.vue'
import pieChart from './components/pieChart.vue'
import fileUploader from './components/fileUploader.vue'
import navTop from './components/navTop.vue'
import floatNav from './components/floatNav.vue'
</script>

<template>
  <body class="mainWindow">
    <floatNav/>
    <div class="left">
      <sideGuide @data-update="handleChange" :activeState="0"/>
    </div>

    <div class="right">
      <navTop/>
      <span class="uploadSection" id="sec1">上传区域</span>
      <div>
        <urlInput @isRunningNewFile="handleUploadNewURL" @isFinishedNewFile="handleUploadURLFinished" @isFinishedAnalyze="handleAnalyzeFinished"/>
      </div>
      <div>
        <fileUploader @uploaded="handleUpload" @fileAnaFinished="handleFileAnaFinished"/>
      </div>
      <span class="commentSection" id="sec2">热评</span>
      <div>
        <commentList :fileState="uploadState" :isSpiding="spidingState"/>
      </div>
      <span class="emotionSection" id="sec3">情绪分析</span>
      <div>
        <textInput @isRunningNewText="handleUploadNewText" @isFinishedNewText="handleTextAnalyzeFinished"/>
      </div>
      <div>
        <barChartC :loadingState="wholeChartRunningState" :provinceData="provinceData"/>
      </div>
      <div :class="{'container': true, 'row': singleChartShowState}">
        <div><pieChart :pScore="WPscore" :nScore="WNscore" :loadingState="wholeChartRunningState"/></div>
        <div v-show="singleChartShowState"><pieChart :loadingState="singleChartRunningState" :titlename="'待分析评论情绪分布'" :pScore="SPscore" :nScore="SNscore"/></div>
      </div>
    </div>
  </body>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      SPscore: 0.5,
      SNscore: 0.5,
      WPscore: 0.5,
      WNscore: 0.5,
      provinceData: [],

      uploadState: false,

      spidingState: false,
      wholeChartRunningState: false,

      singleChartShowState: false,
      singleChartRunningState: false,
    }
  },
  methods: {
    handleChange(data){
      this.$emit('data-update1H', data);
    },

    handleUpload(){
      this.uploadState = !this.uploadState;
      this.wholeChartRunningState = true;
    },
    handleFileAnaFinished() {
      this.wholeChartRunningState = false;
    },

    handleUploadNewURL(){
      this.spidingState = true;
      this.wholeChartRunningState = true;
    },
    handleUploadURLFinished(){
      this.spidingState = false;
    },
    handleAnalyzeFinished(data){
      this.WPscore = data.Wpositive;
      this.WNscore = data.Wnegative;
      this.provinceData = data.provinceResult;
      this.wholeChartRunningState = false;
    },

    handleUploadNewText(){
      this.singleChartShowState = true;
      this.singleChartRunningState = true;
    },
    handleTextAnalyzeFinished(changedData){
      this.SPscore = changedData.pScore;
      this.SNscore = changedData.nScore;
      this.singleChartRunningState = false;
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
  /* height: 600px; */
  height: 100vh;
}

/* 右侧 */
.mainWindow .right {
  flex: 1;
  display: flex; /* 添加flex布局 */
  flex-direction: column; /* 垂直排列子元素 */
  align-items: center; /* 水平居中 */
  margin: 0 auto; /* 水平居中整个.right容器 */
}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.row {
  flex-direction: row;
  justify-content: center;
  gap: 20px;
}
.commentSection{
  width: 100%;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
  padding-top: 20px;
  color: #00ccff;
  border-top: 6px solid #00ccff;
}
.emotionSection {
  width: 100%;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
  margin-top: 120px;
  padding-top: 20px;
  color: #00ccff;
  border-top: 4px solid #00ccff;
}
.uploadSection {
  width: 100%;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
  /* margin-top: 20px; */
  padding-top: 20px;
  color: #00ccff;
  border-top: 4px solid #00ccff;
}
</style>

