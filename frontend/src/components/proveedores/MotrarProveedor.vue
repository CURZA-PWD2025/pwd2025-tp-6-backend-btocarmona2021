<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useProveedoresStore from '@/stores/proveedores'
import { useRouter, useRoute } from 'vue-router'

const { proveedor, proveedores } = toRefs(useProveedoresStore())

const router = useRouter()
const route = useRoute()

watch(proveedores, () => {
    router.push({ name: 'listar_marcas' })
})

onMounted(() => {
    const id = Number(route.params.id)
    proveedor.value = proveedores.value.find((proveedor) => proveedor.id === id) || {
        id: 0,
        nombre: '',
        telefono: '',
        direccion: '',
        email: '',
    }
})
</script>

<template>
  <div class="mostrar-proveedor-container">
    <div class="proveedor-detalle">
      <span><strong>ID:</strong> {{ proveedor.id }}</span>
      <span><strong>Nombre:</strong> {{ proveedor.nombre }}</span>
      <span><strong>Teléfono:</strong> {{ proveedor.telefono }}</span>
      <span><strong>Dirección:</strong> {{ proveedor.direccion }}</span>
      <span><strong>E-mail:</strong> {{ proveedor.email }}</span>
    </div>
    <router-link class="volver-link" :to="{name:'listar_proveedores'}">Volver</router-link>
  </div>
</template>

<style scoped>
.mostrar-proveedor-container {
  max-width: 500px;
  margin: 3rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 1rem;
  color: #2c3e50;
  text-align: center;
}

.proveedor-detalle {
  margin-bottom: 1rem;
  padding: 0.75rem;
  background-color: #f4f6f8;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
}

.volver-link {
  display: inline-block;
  margin-top: 1.5rem;
  padding: 0.6rem 1rem;
  background-color: #4f8cff;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: bold;
  transition: background-color 0.3s ease;
  text-align: center;
}
.volver-link:hover {
  background-color: #2563eb;
}
</style>
