<script setup lang="ts">
import { toRefs, watch, router } from 'vue';
import useMarcasStore from '@/stores/marcas';
import { useRouter } from 'vue-router';
const { marca ,crear, marcas} = toRefs(useMarcasStore());

const router = useRouter()

watch(marcas, () => {
  router.push({name:"listar_marcas"})
})

</script>

<template>
  <div>
    Para Crear Marca
    <form @submit.prevent="crear(marca)">
      <label for="">Nombre de la marca</label>
      <input type="text" name="" v-model="marca.nombre">
      <button>
        Guardar Marca
      </button>
    </form>

    <router-link :to="{name:'listar_marcas'}">Volver</router-link>
  </div>
</template>

<style scoped>

</style>