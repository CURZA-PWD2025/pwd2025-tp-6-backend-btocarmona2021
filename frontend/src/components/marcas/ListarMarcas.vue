<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import useMarcasStore from '@/stores/marcas.ts'
import { Icon } from '@iconify/vue'

const { marcas } = toRefs(useMarcasStore())
const { obtenerTodo, eliminar } = useMarcasStore()

onMounted(async () => {
    await obtenerTodo()
})
</script>

<template>
    <div class="listar-marcas-container">
        <div class="header-row">
            <h2>Listado de Marcas</h2>
            <router-link class="btn primary" :to="{ name: 'crear_marca' }">Crear Marca</router-link>
        </div>
        <table class="styled-table">
            <caption>
                Listado de Marcas
            </caption>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Nombre</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(marca, index) in marcas" :key="index">
                    <td>{{ marca.id }}</td>
                    <td>{{ marca.nombre }}</td>
                    <td>
                        <router-link :to="{ name: 'mostrar_marca', params: { id: marca.id } }">
                            <Icon icon="mdi:show" width="24" height="24" />
                        </router-link>
                        <router-link :to="{ name: 'modificar_marca', params: { id: marca.id } }">
                            <Icon icon="ic:baseline-mode-edit" width="24" height="24" />
                        </router-link>
                        <button class="icon-btn" @click.prevent="eliminar(marca.id)">
                            <Icon
                                icon="material-symbols:delete"
                                width="24"
                                height="24"
                                style="color: darkred"
                            />
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.listar-marcas-container {
    background: #f8fafc;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(79, 140, 255, 0.08);
    padding: 2rem 1.5rem 1.5rem 1.5rem;
    max-width: 700px;
    margin: 2rem auto 0 auto;
}

.header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.btn {
    background: #e0e7ff;
    color: #22223b;
    border: none;
    border-radius: 6px;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition:
        background 0.2s,
        color 0.2s;
    text-decoration: none;
    display: inline-block;
}
.btn.primary {
    background: #4f8cff;
    color: #fff;
}
.btn.primary:hover,
.btn.primary:focus {
    background: #2563eb;
}

.styled-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(79, 140, 255, 0.06);
    font-size: 1rem;
}

.styled-table caption {
    caption-side: top;
    font-size: 1.1rem;
    font-weight: 600;
    color: #22223b;
    margin-bottom: 0.5rem;
    padding: 0.5rem 0;
}

.styled-table th,
.styled-table td {
    padding: 0.85rem 1rem;
    text-align: left;
}

.styled-table thead {
    background: #4f8cff;
    color: #fff;
}

.styled-table tbody tr {
    border-bottom: 1px solid #e0e7ff;
    transition: background 0.2s;
}

.styled-table tbody tr:nth-child(even) {
    background: #f4f8ff;
}

.styled-table tbody tr:hover {
    background: #e0e7ff;
}

.icon-btn {
    background: none;
    border: none;
    padding: 0.2rem;
    margin: 0 0.2rem;
    cursor: pointer;
    vertical-align: middle;
    transition: background 0.2s;
    border-radius: 4px;
}
.icon-btn:hover {
    background: #fbe9e7;
}
</style>
