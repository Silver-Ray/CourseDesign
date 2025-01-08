<template>
  <div class="wholePieChart">
    <div v-show="loadingState" class="loading">加载中...</div>
    <div v-show="!loadingState" ref="chartDom" class="emotionPie"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'pieChart',
  props: {
    titlename: {
      type: String,
      default: '情绪分布玫瑰图'
    },
    pScore: {
      type: Number,
      required: true,
    },
    nScore: {
      type: Number,
      required: true,
    },
    loadingState: {
      type: Boolean,
      required: true,
    }
  },
  data() {
    return {
      chartDom: null,
      myChart: null,
      option: null,
    };
  },
  mounted() {
    this.initChart();
  },
  watch: {
    pScore() {
      this.setOptions();
    },
    nScore() {
      this.setOptions();
    }
  },
  methods: {
    initChart() {
      this.chartDom = this.$refs.chartDom;
      if(!this.chartDom){
        console.error("Chart DOM not found!");
        return;
      }
      this.myChart = echarts.init(this.chartDom);
      this.setOptions();
    },
    setOptions() {
      const option = {
        title: {
          text: this.titlename,
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b} : {d}%'
        },
        legend: {
          bottom: 10,
          left: 'center',
          data: ['positive', 'negative']
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        series: [
          {
            type: 'pie',
            radius: [50, 200],
            center: ['50%', '50%'],
            roseType: 'radius',
            itemStyle: {
              borderRadius: 8
            },
            data: [
              {
                value: this.pScore, name: 'positive', itemStyle: {
                  color: '#FFC125'
                }
              },
              {
                value: this.nScore, name: 'negative', itemStyle: {
                  color: '#4A90E2'
                }
              }
            ]
          }
        ]
      };
      this.myChart.setOption(option);
    }
  },
};
</script>

<style scoped>
.wholePieChart{
  margin: 40px 0;
}
/* 情绪分布饼图规格 */
.wholePieChart .emotionPie {
  width: 600px;
  height: 550px;
  border: 2px solid #000;
  border-radius: 10px;
  background-color: #f3f5f7;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 600px;
  height: 550px;
  border: 2px solid #000;
  border-radius: 10px;
  font-size: 24px;
  font-weight: bold;
  color: #555;
  background-color: #fff;
}
</style>