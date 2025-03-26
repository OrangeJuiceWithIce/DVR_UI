<template>
    <div>
        <input type="file" @change="handleFileSelect">
    </div>
</template>

<script>
    export default {
        name: 'FileUpload',
        methods: {
            handleFileSelect(event) {
                const file = event.target.files[0];
                this.$emit('file-selected', file);
            }
        }
    }
</script>

<style scoped>
input{
    margin-top: 10px;
}
</style>