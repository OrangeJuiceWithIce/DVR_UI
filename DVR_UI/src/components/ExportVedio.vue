<template>
    <div class="export-video-button" @click="exportVideo()">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="black"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="feather feather-download"
      >
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
        <polyline points="21 8 12 13 3 8"></polyline>
      </svg>
    </div>
</template>

<script>
export default{
    methods:{
        exportVideo(){
            this.$emit('export-video')
        }
    }
}
</script>

<style scoped>
.export-video-button {
  padding: 5px 10px;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: white;
  opacity: 0.3;
  transition: box-shadow 0.3s ease; /* 添加过渡效果 */
  transition: opacity 0.5s ease; /* 添加过渡效果 */
}

.export-video-button:hover {
  opacity: 0.8;
  box-shadow: 0 0 10px #888;
}
</style>