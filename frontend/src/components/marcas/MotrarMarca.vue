<script setup lang="ts">
import useMarcasStore from '@/stores/marcas.ts'
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const { marca, marcas } = toRefs(useMarcasStore())
const routes = useRoute()

onMounted(() => {
    const id = Number(routes.params.id)
    marca.value = marcas.value.find((marca) => marca.id === id) || { id: 0, nombre: '' }
    
})
</script>

<template>
    <div>
        <div>
            {{ marca.id }}
            {{ marca.nombre }}
        </div>
        <router-link :to="{name:'listar_marcas'}">Volver</router-link>
    </div>
</template>

<style scoped>
div {
  max-width: 500px;
  margin: 3rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 1rem;
  color: #2c3e50;
}

div > div {
  margin-bottom: 1rem;
  padding: 0.75rem;
  background-color: #f4f6f8;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  font-weight: bold;
}

router-link {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.6rem 1rem;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: bold;
  transition: background-color 0.3s ease;
  text-align: center;
}

router-link:hover {
  background-color: #2980b9;
}
</style>
