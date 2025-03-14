<template>
  <div id="app">
    <div class="input-and-checkpoint">
      <!--检查点组件-->
      <CheckPoint :currentStep="currentStep" @change-step="currentStepChange" ref="checkPoint"/>
      <!-- 输入组件 -->
      <TextInput @submitText="handleSubmitText"/>
    </div>
    <!-- 结果展示组件 -->
    <ExplorationResults :results="results" :separateResults="separateResults" :filterResults="filterResults" 
    @activeImageChanged="activeImageChanged" 
    @activeGaussianChanged="activeGaussianChanged"
    @filterGaussian="handleFilterGaussians"
    />
    <ExportVedio @exportVideo="handleExportVideo"></ExportVedio>
  </div>
</template>

<script>
import TextInput from './components/TextInput.vue';
import ExplorationResults from './components/ExplorationResults.vue';
import CheckPoint from './components/CheckPoint.vue';
import ExportVedio from './components/ExportVedio.vue';

export default {
  components: {
    TextInput,
    ExplorationResults,
    CheckPoint,
    ExportVedio,
  },
  data() {
    return {
      results: [], // 存储从后端获取的结果
      separateResults: [], //分割特征
      userInput: '', // 用户输入的文本
      activeId: 0, // 当前激活的TF的ID
      activeGaussianId: [], // 当前激活的高斯的ID
      filterResults:[],  // api6过滤后的高斯结果
      currentStep: 0, // 当前步骤
    };
  },
  methods: {
    activeImageChanged(id){
      this.activeId=id;
      this.handleSeparateGaussians(); // 切换图片时分割高斯
    },
    activeGaussianChanged(activeGaussians){
      this.activeGaussianId=activeGaussians;
    },
    currentStepChange(step) {
      this.currentStep=step;
      this.getPopulationCheckpoint(); // 切换step时刷新
    },

    async handleSubmitText(text) {
      this.userInput = text;
      let sort=0;
      console.log(this.activeGaussianId);
      if(this.userInput===''){
        if(this.activeGaussianId.length!=this.separateResults.length){
          alert('请输入文本');
          return;
        }
        else{
          this.handleGetExplorationResults();//explore
          sort=1;
        }
      }
      else{
        if(this.activeGaussianId.length===this.separateResults.length){
          this.handleGetTextStyleGuideResults();//text guide
          sort=2;
        }
        else{
          this.handleTextRegionGuide(); //text and region guide
          sort=3;
        }
      }
      this.currentStep+=1; // 切换step
      this.$refs.checkPoint.addCheckPoint(sort); // 添加检查点
    },

    // api 1
    async handleGetExplorationResults() {
      try {
        const response = await fetch('http://127.0.0.1:5000/get_exploration_results', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            selected_number: 4, // 默认选择前4个结果
          }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        this.results = data; // 更新结果数据
        this.handleSeparateGaussians(0); // 默认分割第一个TF的高斯
      } catch (error) {
        console.error('Error fetching initial exploration results:', error);
        alert('Failed to load initial results. Please check the server URL and try again.');
      }
    },

    //api 2
    async handleGetTextStyleGuideResults(){
      try {
          const response = await fetch('http://127.0.0.1:5000/get_text_style_guide_results', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              text: this.userInput,
              selected_number: 4,
              one_epoch: 5,
            }),
          });
  
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
  
          const data = await response.json();
          this.results = data; // 更新结果数据
          if (data.length > 0) {
            this.handleSeparateGaussians(0); // 假设分割第一个TF的高斯
          }
        } catch (error) {
          console.error('Error submitting text:', error);
          alert('Failed to submit text. Please check the server URL and try again.');
        }
    },

    //api 5
    async handleSeparateGaussians() {
      try {
        const response = await fetch('http://127.0.0.1:5000/get_seperate_gaussians', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            tfparams: this.results[this.activeId], // 发送 activeId 到后端
          }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        this.separateResults = data; // 更新高斯分解结果
      } catch (error) {
        console.error('Error fetching gaussian results:', error);
        alert('Failed to fetch gaussian results. Please check the server URL and try again.');
      }
    },

    //api6
    async handleFilterGaussians(actualMarker){
      try{
        const response = await fetch('http://127.0.0.1:5000/filter_gaussians_by_region', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            region:actualMarker,
            tfparams: this.results[this.activeId], // 发送当前激活的TFparams
          }),
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        this.filterResults = data; // 更新高斯过滤结果
      }catch(error){
        console.error('Error fetching filtered gaussians:', error);
        alert('Failed to fetch filtered gaussians. Please check the server URL and try again.');
      }
    },

    //api 7
    async handleTextRegionGuide() {
      try {
        const response = await fetch('http://127.0.0.1:5000/get_text_region_guide_results', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            text: this.userInput,
            tfparams: this.results[this.activeId], // 发送当前激活的TFparams
            selected_gaussian_ids: this.activeGaussianId, // 发送当前激活的高斯ID
            selected_number: 4,
            one_epoch: 5,
          }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        this.results = data; // 更新结果数据
        if (data.length > 0) {
          this.handleSeparateGaussians(); // 假设分割第一个TF的高斯
        }
      } catch (error) {
        console.error('Error fetching region guide results:', error);
        alert('Failed to fetch region guide results. Please check the server URL and try again.');
      }
    },
    //api 8
    async getPopulationCheckpoint(){
      try{
        const response = await fetch('http://127.0.0.1:5000/get_population_checkpoint', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            iteration: this.currentStep,
            selected_number: 4,
          }),
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        this.results = data; // 更新结果数据
        if (data.length > 0) {
          this.handleSeparateGaussians(0); // 假设分割第一个TF的高斯
        }
      }catch(error){
        console.error('Error fetching population checkpoint:', error);
        alert('Failed to fetch population checkpoint. Please check the server URL and try again.');
      }
    },
    //api9
    async handleExportVideo(){
      try{
        const response = await fetch('http://127.0.0.1:5000/export_tf_video', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            tfparams: this.results[this.activeId], // 发送当前激活的TFparams
          }),
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const blob=await response.blob();

        const url=window.URL.createObjectURL(blob);
        const a=document.createElement('a');
        a.style.display='none';
        a.href=url;
        a.download='tf_video.mp4';

        document.body.appendChild(a);
        a.click();

        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      }catch(error){
        console.error('Error exporting video:', error);
        alert('Failed to export video. Please check the server URL and try again.');
      };
    },
  },
  mounted() {
    this.handleGetExplorationResults(); // 页面加载时发起请求
  },
};
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
}
.input-and-checkpoint {
  display: flex;
  gap: 20px;
  align-items: center;
}
</style>