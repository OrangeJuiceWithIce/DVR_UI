<template>
    <div class="text-input-container">
      <div class="text-input-wrapper">
        <input type="text" id="user-input" v-model="userInput" placeholder="describe or upload an image">
      <div class="file-upload-button" @click="triggerFileInput">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="feather feather-upload"
        >
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
          <polyline points="17 8 12 3 7 8"></polyline>
          <line x1="12" y1="3" x2="12" y2="15"></line>
        </svg>
      </div>
      </div>
      <input type="file" ref="fileInput" @change="handleFileSelect" class="hidden-file-input">
      <div @click="submitText" class="text-input-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="feather feather-send"
        >
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
        Query
      </div>
      <!-- <button @click="submitText">Query</button> -->
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userInput: '', // 用户输入的语言指令
      };
    },
    methods: {
      async submitText() {
        this.$emit('submitText',this.userInput)
      },
      triggerFileInput() {
        this.$refs.fileInput.click(); // 触发文件输入框的点击事件
      }
    },
  };
  </script>
  
  <style scoped>
  .text-input-container {
    margin: 5px;
    display:flex;
    align-items:center;
    column-gap: 5px;
  }
  
  .text-input-container label {
    margin-right: 10px;
  }
  
  .text-input-container input {
    padding: 10px;
    width:230px;
    border:none;
    outline: none;
  }

  .text-input-wrapper{
    display:flex;
    align-items: center;
    justify-content: center;
    column-gap: 3px;
    border:1px solid #ccc;
    border-radius:5px;
  }
  
  .text-input-button{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 80px;
    height: 30px;
    border-radius:5px;
    border:1px solid #ccc;
    cursor:pointer;
    transition: box-shadow 0.3s ease; /* 添加过渡效果 */
  }

  .text-input-button:hover{
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  }
  
  .text-input-container button {
    padding: 10px 20px;
    background-color: #0073e6;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .file-upload-button{
    display: flex;
    width:30px;
    height:30px;
    border-radius: 5px;
    align-items: center;
    justify-content: center;
    transition: box-shadow 0.3s ease; /* 添加过渡效果 */
    cursor:pointer;
  }

  .file-upload-button:hover{
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  }

  .text-input-container button:hover {
    background-color: #005bb5;
  }

  .hidden-file-input{
    display: none;
  }
  </style>