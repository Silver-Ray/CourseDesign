<template>
  <div class="wholeUploader">
    <a-upload-dragger
      v-model:fileList="fileList"
      name="file"
      :multiple="true"
      action="http://localhost:8000/api/fileUpload/"
      @change="handleChange"
      @drop="handleDrop"
    >
      <p class="ant-upload-drag-icon">
        <inbox-outlined></inbox-outlined>
      </p>
      <p class="ant-upload-text">点击或拖拽文件到此区域上传</p>
      <p class="ant-upload-hint">
        支持单或批文件
      </p>
    </a-upload-dragger>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { InboxOutlined } from '@ant-design/icons-vue';
import { message } from 'ant-design-vue';
import axios from 'axios';

const emit = defineEmits(['uploaded', 'fileAnaFinished']);

const fileList = ref([]);

// 定义延迟函数
const delay = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

// 处理文件上传状态变化
const handleChange = async (info) => {
  const status = info.file.status;
  if (status !== 'uploading') {
    console.log(info.file, info.fileList);
  }
  if (status === 'done') {
    message.success(`${info.file.name} file uploaded successfully.`);
    console.log("Response:", info.file.response);
    emit('uploaded');

    try {
      const response1 = await axios.get('http://localhost:8000/api/isFileAnalyzeFinished/');
      await delay(1000);
      emit('fileAnaFinished', response1.data);
    } catch (error) {
      console.error('Error fetching file analysis result:', error);
    }
  } else if (status === 'error') {
    message.error(`${info.file.name} file upload failed.`);
  }
};

// 处理拖放事件
const handleDrop = (e) => {
  console.log(e);
};
</script>

<style scoped>
.wholeUploader {
  width: 500px;
  height: 160px;
  background-color: #fff;
  border: 2px solid #000;
  border-radius: 10px;
}
</style>