<template>
    <div class="container">
      <!-- 颜色说明区域 -->
      <div class="legend">
        <div
          v-for="button in legend"
          :key="button.id"
          class="legend-item"
        >
          <div
            class="legend-circle"
            :style="{ backgroundColor: button.color }"
          ></div>
          <span>{{ button.description }}</span>
        </div>
      </div>
      <!-- 圆形按钮区域 -->
      <div class="button-group">
        <div
          v-for="(button, index) in buttons"
          :key="button.id"
          class="button-item"
          :class="{ active: activeButtonId === button.id }"
          @click="setActiveStep(button.id)"
        >
          <div
            class="circle-button"
            :style="{ backgroundColor: button.color }"
          ></div>
          <!-- 在按钮之间添加线条 -->
          <div v-if="index < buttons.length - 1" class="line"></div>
        </div>
        <span class="active-step">current step:{{ activeButtonId }}</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeButtonId: 1,
        buttons: [
          { id: 1, color: '#FFCDD2', description: 'exploration' },
          { id: 2, color: '#FFCDD2', description: 'exploration' },
          { id: 3, color: '#FFCDD2', description: 'exploration' },
          { id: 4, color: '#C8E6C9', description: 'styling' },
          { id: 5, color: '#C8E6C9', description: 'styling' },
          { id: 6, color: '#BBDEFB', description: 'fine-tuning' },
          { id: 7, color: '#C8E6C9', description: 'styling' },
          { id: 8, color: '#C8E6C9', description: 'styling' },
        ],
        legend:[
          { id: 1, color: '#FFCDD2', description: 'exploration' },
          { id: 2, color: '#C8E6C9', description: 'styling' },
          { id: 3, color: '#BBDEFB', description: 'fine-tuning' },
        ]
      };
    },
    methods:{
        setActiveStep(id) {
            this.activeButtonId = id;
            this.$emit('change-step', id);
        }
    }
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .button-group {
    display: flex;
    align-items: center;
  }

  .button-item {
    display:flex;
    flex-direction: row;
    z-index: 1;
  }
  
  .circle-button {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin: 0;
  }
  
  .line {
    width: 30px;
    height: 2px;
    background-color: #ccc;
    position: relative;
    top: 10px; /* 对齐线条和按钮 */
    z-index: 0;
  }

  /* 激活状态样式 */
  .active .circle-button {
    transform: scale(1.2); /* 放大按钮 */
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.4); /* 更强烈的阴影 */
    border: 2px solid #999898; /* 添加深色边框 */
    background-color: lighten(currentColor, 20%); /* 背景颜色变亮 */
    z-index: 1;
  }

    /* 鼠标悬停样式 */
  .button-item:hover .circle-button {
    transform: scale(1.1); /* 放大按钮 */
    cursor: pointer;
  }
  
  .legend {
    display: flex;
  }
  
  .legend-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    margin-right:5px;
  }
  
  .legend-circle {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .active-step {
    font-size: 16px;
    margin-left:10px;
  }
  </style>