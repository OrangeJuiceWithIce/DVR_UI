<template>
  <div class="exploration-container">
    <!-- 左侧缩略图列表 -->
    <div class="thumbnail-list">
      <div
        v-for="result in results"
        :key="result.id"
        class="thumbnail-item"
        :class="{ active: result.id === activeId }"
        @click="setActiveImage(result.id)"
      >
        <img :src="'data:image/*;base64,'+result.image" alt="Thumbnail" class="thumbnail">
      </div>
    </div>

    <!-- 主图展示 -->
    <div class="main-image" @click="addMarker($event)" @mouseenter="ifHoverMainImage=true" @mouseleave="ifHoverMainImage=false" @wheel="handleWheel($event)">
      <img :src="'data:image/*;base64,'+activeImage" alt="Main Image" class="main-image-content">
      <!-- 动态显示标记点 -->
      <div
        v-if="marker"
        class="marker"
        :style="{ top: marker.y + 'px', left: marker.x + 'px' }"
      ></div>
    </div>

    <!-- 高斯分解结果列表 -->
    <div class="gaussian-list">
      <div v-if="separateResults.length > 0">
        <div
          v-for="gaussian in separateResults"
          :key="gaussian.id"
          class="gaussian-item"
          :class="{ active:isActivated(gaussian.id)}"
          @click="setActiveGaussian(gaussian.id)"
        >
          <img :src="'data:image/*;base64,'+gaussian.image" alt="Gaussian Image" class="gaussian-image">
          <input
          type="checkbox"
          class="checkbox"
          :checked="isActivated(gaussian.id)"
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    results: {
      type: Array,
      required: true,
    },
    separateResults: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      activeId: null, // 当前激活的图片 ID
      activeImage: '', // 当前展示的主图
      marker: null, // 标记点
      actualMarker:null,  //实际相对于图片的位置
      ifHoverMainImage:false, //鼠标是否在主图上
      wheelTimeout:null, //防止滚动过快
    };
  },
  watch: {
    // 监听 results 的变化，默认显示第一张图片
    results(newResults) {
      if (newResults.length > 0) {
        this.activeId = newResults[0].id;
        this.activeImage = newResults[0].image;
        this.$emit('activeImageChanged', this.activeId);
      }
    },
  },
  methods: {
    isActivated(gaussianId){
      for(let gaussian of this.results.find(result => result.id === this.activeId).gaussians){
        if (gaussian.id === gaussianId && gaussian.activate){
          return true;
        }
      }
      return false;
    },
    setActiveImage(id) {
      const selectedResult = this.results.find(result => result.id === id);
      if (selectedResult) {
        this.activeId = id;
        this.activeImage = selectedResult.image;
        this.marker = null; // 清除之前的标记点
        this.actualMarker=[];
        this.$emit('activeImageChanged', id);
      }
    },
    setActiveGaussian(id) {
      console.log(id)
      this.results.find(result => result.id === this.activeId).gaussians.forEach(gaussian => {
        if (gaussian.id === id) {
          gaussian.activate = !gaussian.activate;
          this.$emit('activeGaussianChanged', this.results);
        } 
      });
    },
    addMarker(event) {
      // 获取图片容器的 DOM 元素
      const container = event.currentTarget;

      // 获取图片容器的边界框
      const rect = container.getBoundingClientRect();

      // 获取点击位置的坐标（相对于容器）
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      
      const imgElement = container.querySelector('img');
      const scaleX = imgElement.naturalWidth / imgElement.clientWidth;
      const scaleY = imgElement.naturalHeight / imgElement.clientHeight;

      // 更新标记点的位置
      this.marker = { x , y };
      this.actualMarker={'x':x*scaleX,'y':y*scaleY};
      this.$emit('filterGaussian', this.actualMarker);
    },
    handleWheel(event) {
      if (this.wheelTimeout){
        return;
      }
      this.wheelTimeout = setTimeout(() => {
        let direction = event.deltaY;
        this.$emit('handleWheel',direction);
        this.wheelTimeout = null;
      },1000);
    },
  },
  mounted() {
    // 默认显示第一张图片
    if (this.results.length > 0) {
      this.activeId = this.results[0].id;
      this.activeImage = this.results[0].image;
      this.$emit('activeImageChanged', this.activeId);
    }
  },
};
</script>

<style scoped>
.exploration-container {
  display: flex;
  gap: 20px;
  width: 800px; /* 固定容器宽度 */
  height: 500px; /* 固定容器高度 */
  margin: 0 auto; /* 居中显示 */
}

.thumbnail-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 150px; /* 固定宽度 */
  height: 400px; /* 固定高度 */
  overflow-y: auto; /* 允许垂直滚动 */
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.thumbnail-item {
  position: relative; /* 确保标注的绝对定位是相对于这个容器 */
  width: 120px; /* 固定宽度 */
  height: 120px; /* 固定高度 */
  cursor: pointer;
  border: 3px solid transparent;
  border-radius: 5px;
  transition: border-color 0.3s ease;
}

.thumbnail-item.active {
  border-color: #0073e6;
}

.thumbnail-item:hover {
  border-color: #005bb5;
}

.thumbnail {
  width: 100%;
  height: 100%;
  border-radius: 5px;
  object-fit: cover; /* 确保图片填充整个容器 */
}

.main-image {
  display: flex;
  justify-content: center;
  align-items: center;
  border: 2px solid #343131;
  padding: 0;
  border-radius: 10px;
  width: 400px; /* 固定宽度 */
  height: 400px; /* 固定高度 */
  position: relative;
  overflow: hidden; /* 防止内容溢出 */
}

.main-image-content {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  object-fit: contain; /* 保持图片比例 */
}

.gaussian-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 150px; /* 固定宽度 */
  height: 400px; /* 固定高度 */
  overflow-y: auto; /* 允许垂直滚动 */
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.gaussian-item {
  position: relative; /* 确保标注的绝对定位是相对于这个容器 */
  width: 120px; /* 固定宽度 */
  height: 120px; /* 固定高度 */
  cursor: pointer;
  border: 3px solid transparent;
  border-radius: 5px;
  transition: border-color 0.3s ease;
}

.gaussian-item.active {
  border-color: #0073e6;
}

.gaussian-item:hover {
  border-color: #005bb5;
}

.gaussian-image {
  width: 100%;
  height: 100%;
  border-radius: 5px;
  object-fit: cover; /* 确保图片填充整个容器 */
}

.marker {
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: red;
  border-radius: 50%;
  transform: translate(-50%, -50%); /* 使标记点居中于点击位置 */
}

.checkbox {
  position: absolute;
  top: 5px; /* 距离顶部的距离 */
  right: 5px; /* 距离右侧的距离 */
  z-index: 100;
  width: 20px;
  height: 20px;
  border: 2px solid #ccc;
  border-radius: 4px;
  appearance: none; /* 移除默认样式 */
  background-color: white; /* 默认背景颜色 */
  cursor: pointer;
}

.checkbox:checked {
  background-color: #0073e6; /* 激活状态的背景颜色 */
}

.checkbox:checked::after {
  content: '\2713'; /* 使用 Unicode 字符表示打勾 */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 14px;
  font-weight: bold;
}
</style>