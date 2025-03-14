<template>
    <div class="text-input-container">
      <label for="user-input">Text Input:</label>
      <input type="text" id="user-input" v-model="userInput" placeholder="please input your text">
      <button @click="submitText">next step</button>
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
      }
    },
  };
  </script>
  
  <style scoped>
  .text-input-container {
    margin: 5px;
  }
  
  .text-input-container label {
    margin-right: 10px;
  }
  
  .text-input-container input {
    margin-right: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .text-input-container button {
    padding: 10px 20px;
    background-color: #0073e6;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .text-input-container button:hover {
    background-color: #005bb5;
  }
  </style>