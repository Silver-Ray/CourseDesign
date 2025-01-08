<template>
  <div class="wholeBarChart">
    <div id="provinceBar"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

// 导入JSON文件
import provinceData from '/public/data/province.json';

export default {
  name: 'barChart',
  props: {
    titlename: {
      type: String,
      default: "省份情绪分布柱状图"
    }
  },
  data() {
    return {
      myChart: null,
      option: null,
    };
  },
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const chartDom = document.getElementById('provinceBar');
      this.myChart = echarts.init(chartDom);
      this.myChart.showLoading();

      // 使用导入的JSON数据
      this.setOptions(provinceData);
      this.myChart.hideLoading();
    },
    setOptions(data) {
      const provinces = data.map(item => item.province); // 提取province作为x轴标签
      const positives = data.map(item => item.positive); // 提取positive作为正向数据
      const negatives = data.map(item => item.negative); // 提取negative作为负向数据

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
  margin: 20px 0;
}
.wholeBarChart #provinceBar {
  width: 800px;
  height: 500px;
  border: 2px solid #000;
  border-radius: 10px;
  background-color: #f3f5f7;
}
</style>