<script setup lang="ts">
import { RouterView, useRouter} from 'vue-router';
import { onMounted } from 'vue';

const route = useRouter()

onMounted(() => {
  route.push({ name:'listar_articulos'})
})
</script>
<template>
  <div>
    <RouterView/>
  </div>
</template>


<style scoped>

</style>