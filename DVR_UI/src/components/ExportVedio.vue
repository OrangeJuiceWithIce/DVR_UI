<template>
    <button @click="exportVideo">Export Video</button>
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
button {
  padding: 10px 20px;
  background-color: #0073e6;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left:350px;
  height:40px;
  width:120px;
}

button:hover {
  background-color: #005bb5;
}
</style>