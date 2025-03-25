<template>
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
</template>

<script>
    export default {
        data(){
            return{
                legend: [
                    { id: 1, color: '#FFCDD2', description: 'Exploration' },
                    { id: 2, color: '#C8E6C9', description: 'Customization' },
                    { id: 3, color: '#BBDEFB', description: 'Refinement' },
                ],
            }
        }
    }
</script>

<style scoped>
  .legend {
    margin-right: 40px;
    padding-top: 7px;
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
</style>