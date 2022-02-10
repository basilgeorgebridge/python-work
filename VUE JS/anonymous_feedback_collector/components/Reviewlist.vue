<template>
  <div class="content">
    <div>{{ review }}</div>
  </div>
</template>
<script>
export default {
  props: ["review"],
};
</script>
<style scoped>
.content {
  border: 1px solid green;
  margin: 10px 0px;
}
</style>
