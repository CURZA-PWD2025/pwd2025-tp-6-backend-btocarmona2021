<script setup lang="ts">
import useCategoriasStore from '@/stores/categorias'
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const { categoria, categorias } = toRefs(useCategoriasStore())
const routes = useRoute()

onMounted(() => {
    const id = Number(routes.params.id)
    categoria.value = categorias.value.find((marca) => marca.id === id) || { id: 0, nombre: '' }
})
</script>

<template>
    <div class="mostrar-categoria-container">
        <div class="categoria-detalle">
            <span>ID: {{ categoria.id }}</span>
            <span>Nombre: {{ categoria.nombre }}</span>
        </div>
        <router-link class="volver-link" :to="{ name: 'listar_categorias' }">Volver</router-link>
    </div>
</template>

<style scoped>
.mostrar-categoria-container {
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

.categoria-detalle {
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
    margin-top: 1rem;
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
