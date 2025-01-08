<template>
  <div class="wholeBarChart">
    <div v-show="loadingState" class="loading">加载中...</div>
    <div v-show="!loadingState" id="provinceBar"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import axios from 'axios';

export default {
  name: 'barChart',
  props: {
    titlename: {
      type: String,
      default: "省份情绪分布柱状图",
    },
    loadingState: {
      type: Boolean,
      default: false,
    },
    provinceData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      myChart: null,
      option: null,
      initData: [],
    };
  },
  async mounted() {
    try {
      this.initData = await this.getData();
      if( this.initData )
        this.initChart( this.initData );
      else
        console.log("no data");
    }
    catch(error) {
      console.error("Error initializing chart:", error);
    }
  },
  watch: {
    provinceData() {
      this.setOptions(this.provinceData);
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/api/provinceData/');
        console.log(response.data);
        return response.data;
      }
      catch(error) {
        console.error(error);
        return null;
      }
    },
    initChart(Data) {
      const chartDom = document.getElementById('provinceBar');
      if( !chartDom ){
        console.log("no chartDom");
        return;
      }

      this.myChart = echarts.init(chartDom);
      this.myChart.showLoading();

      // 使用导入的JSON数据
      this.setOptions(Data);
      this.myChart.hideLoading();
    },
    setOptions(Data) {
      const provinces = Data.map(item => item.province); // 提取province作为x轴标签
      const positives = Data.map(item => item.positive); // 提取positive作为正向数据
      const negatives = Data.map(item => item.negative); // 提取negative作为负向数据

      this.option = {
        title: {
          text: this.titlename,
          left: 'center'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow',
            label: {
              show: true
            }
          }
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        calculable: true,
        legend: {
          bottom: 5,
          data: ['Positive', 'Negative'],
          itemGap: 5
        },
        grid: {
          top: '12%',
          left: '1%',
          right: '10%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: provinces, // 使用province作为x轴标签
            axisLabel: {
              rotate: 45, // 旋转标签，角度为45度
              interval: 0, // 显示所有标签
              formatter: '{value}' // 确保标签显示完整
            },
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: 'Values',
            axisLabel: {
              formatter: function (a) {
                a = +a;
                return isFinite(a) ? echarts.format.addCommas(a) : '';
              }
            }
          }
        ],
        series: [
          {
            name: 'Negative',
            type: 'bar',
            data: negatives.map((neg, index) => ({value: neg, name: provinces[index]})), // 包含省份名
            itemStyle: {
              color: '#5470C6' // 蓝色
            }
          },
          {
            name: 'Positive',
            type: 'bar',
            data: positives.map((pos, index) => ({value: pos, name: provinces[index]})), // 包含省份名
            itemStyle: {
              color: '#FFC125' // 橙黄色
            }
          }
        ]
      };
      this.myChart.setOption(this.option);
    }
  }
};
</script>

<style scoped>
.wholeBarChart {
  margin: 20px 0 50px;
}

.wholeBarChart #provinceBar {
  width: 800px;
  height: 500px;
  border: 2px solid #000;
  border-radius: 10px;
  background-color: #f3f5f7;
}

.loading {
  display: flex;
  width: 800px;
  height: 500px;
  border: 2px solid #000;
  border-radius: 10px;
  background-color: #f3f5f7;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  font-weight: bold;
  color: #555;
}
</style>