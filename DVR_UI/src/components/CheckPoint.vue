<template>
    <div class="container">
      <!-- 颜色说明区域 -->
      <div class="legend">
        <div
          v-for="item in legend"
          :key="item.id"
          class="legend-item"
        >
          <div
            class="legend-circle"
            :style="{ backgroundColor: item.color }"
          ></div>
          <span>{{ item.description }}</span>
        </div>
      </div>
  
      <!-- 圆形按钮区域 -->
      <div class="button-group">
        <div class="button-items">
          <div
            v-for="(checkpoint, index) in checkpoints"
            :key="checkpoint.id"
            class="button-item"
            :class="{ active: checkpoint.id === currentStep,
              large:ShouldBeLarge(index)
            }"
            @click="setActiveStep(checkpoint.id)"
          >
            <div
              class="circle-button"
              :style="{ backgroundColor: checkpoint.color }"
            ></div>
            <!-- 在按钮之间添加线条 -->
            <div v-if="index < checkpoints.length - 1" class="line"></div>
          </div>
        </div>
        <span class="active-step">Current Step: {{ currentStep }}</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props:{
      currentStep:{
        type:Number,
        required:true,
      },
    },
    data() {
      return {
        checkpoints: [], // 检查点列表
        legend: [
          { id: 1, color: '#FFCDD2', description: 'Exploration' },
          { id: 2, color: '#C8E6C9', description: 'Customization' },
          { id: 3, color: '#BBDEFB', description: 'Refinement' },
        ],
      };
    },
    methods: {
      setActiveStep(id) {
        this.$emit('change-step', id);
      },
      addCheckPoint(sort,step) {
        // 清除当前步骤之后的所有检查点
        this.checkpoints = this.checkpoints.filter(cp => cp.id < step);
        // 添加新的检查点
        const newCheckpoint = this.legend[sort-1];
        this.checkpoints.push({
          id: step,
          color: newCheckpoint.color,
          description: newCheckpoint.description,
        });
      },
      ShouldBeLarge(index) {
        if(index===this.checkpoints.length-1){
          return true;
        }
        const currentCheckpoint = this.checkpoints[index];
        const nextCheckpoint = this.checkpoints[index + 1];
        if(currentCheckpoint.description!=nextCheckpoint.description){
          return true;
        }
        let count = 1;
        for(let i=index-1;i>=0;i--){
          if(this.checkpoints[i].description===currentCheckpoint.description){
            count++;
            if (this.ShouldBeLarge(i)){
              return false;
            }
          }else{
            break;
          }
        }
        return count===5;
      }
    },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 5px;
    max-width: 800px;
    margin: 0;
  }
  
  .button-group {
    display: flex;
    align-items: center;
  }
  
  .button-items {
    display: flex;
    flex-direction: row;
    width: 235px;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding:5px;
    height:45px;
    overflow-x: auto;
    overflow-y: hidden;
  }

  .button-item {
    display: flex;
    flex-direction: row;
    z-index: 1;
  }
  
  .circle-button {
    width: 15px;
    height: 15px;
    border-radius: 50%;
    margin: 0;
    z-index: 1;
  }
  
  .line {
    width: 15px;
    height: 2px;
    background-color: #ccc;
    position: relative;
    top: 7.5px; /* 对齐线条和按钮 */
    z-index: 0;
  }

  .large .line{
    width:30px;
  }
  
  /* 激活状态样式 */
  .active .circle-button {
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1); /* 更强烈的阴影 */
    border: 2px solid #999898; /* 添加深色边框 */
    background-color: lighten(currentColor, 20%); /* 背景颜色变亮 */
    z-index: 1;
  }

  .large .circle-button {
    transform: scale(1.3); /* 放大按钮 */
  }
  
  /* 鼠标悬停样式 */
  .button-item:hover .circle-button {
    transform: scale(1.1); /* 放大按钮 */
    cursor: pointer;
  }

  .button-item.large:hover .circle-button {
    transform: scale(1.4); /* 放大按钮 */
  }
  
  .legend {
    display: flex;
  }
  
  .legend-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    margin-right: 5px;
  }
  
  .legend-circle {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .active-step {
    font-size: 16px;
    margin-left: 10px;
  }
  </style>