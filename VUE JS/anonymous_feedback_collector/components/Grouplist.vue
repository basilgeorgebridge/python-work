<template>
  <div class="content">
    <div>{{ group }}</div>
  </div>
</template>
<script>
export default {
  props: ["group"],
};
</script>
<style scoped>
.content {
  border: 1px solid green;
  margin: 10px 0px;
}
</style>