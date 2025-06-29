<script setup lang="ts">
import useArticulosStore from '@/stores/articulos'
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const { articulo, articulos } = toRefs(useArticulosStore())
const routes = useRoute()

onMounted(() => {
    const id = Number(routes.params.id)
    articulo.value = articulos.value.find((articulo) => articulo.id === id) || {
        id: 0,
        descripcion: '',
        precio: '',
        stock: 0,
        marca: { id: 0, nombre: '' },
        proveedor: { id: 0, nombre: '', direccion: '', email: '', telefono: '' },
        categorias: [],
    }
})
</script>

<template>
    <div class="mostrar-container">
        <div class="mostrar-datos">
            <div><strong>ID:</strong> {{ articulo.id }}</div>
            <div><strong>Descripción:</strong> {{ articulo.descripcion }}</div>
            <div><strong>Precio:</strong> {{ articulo.precio }}</div>
            <div><strong>Stock:</strong> {{ articulo.stock }}</div>
            <div><strong>Marca:</strong> {{ articulo.marca.nombre }}</div>
            <div><strong>Proveedor:</strong> {{ articulo.proveedor.nombre }}</div>
            <div><strong>Dirección:</strong> {{ articulo.proveedor.direccion }}</div>
            <div><strong>Email:</strong> {{ articulo.proveedor.email }}</div>
            <div><strong>Teléfono:</strong> {{ articulo.proveedor.telefono }}</div>
        </div>
        <router-link :to="{ name: 'listar_articulos' }" class="volver-link">Volver</router-link>
    </div>
</template>

<style scoped>
.mostrar-container {
    max-width: 420px;
    margin: 2.5rem auto;
    padding: 2rem 2.5rem;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.mostrar-datos {
    display: flex;
    flex-direction: column;
    gap: 0.7rem;
    margin-bottom: 1.5rem;
}

.mostrar-datos > div {
    background: #f7f9fa;
    border-radius: 6px;
    padding: 0.6rem 1rem;
    border: 1px solid #e3e7ea;
    font-size: 1rem;
    color: #34495e;
}

.mostrar-datos strong {
    color: #2980b9;
    font-weight: 600;
    margin-right: 0.5rem;
}

.volver-link {
    display: inline-block;
    padding: 0.5rem 1.2rem;
    background: #3498db;
    color: #fff;
    border-radius: 7px;
    text-decoration: none;
    font-weight: 500;
    text-align: center;
    transition: background 0.2s;
}

.volver-link:hover {
    background: #217dbb;
}
</style>
