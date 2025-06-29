<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useCategoriasStore from '@/stores/categorias'
import { useRouter, useRoute } from 'vue-router'

const { categoria, categorias } = toRefs(useCategoriasStore())
const { modificar } = useCategoriasStore()
const router = useRouter()
const route = useRoute()

watch(categorias, () => {
    router.push({ name: 'listar_categgorias' })
})

onMounted(() => {
    const id = Number(route.params.id)
    categoria.value = categorias.value.find((categoria) => categoria.id === id) || {
        id: 0,
        nombre: '',
    }
})
</script>

<template>
    <div class="modificar-categoria-container">
        <h2>Modificar Categoría</h2>
        <form class="modificar-categoria-form" @submit.prevent="modificar(categoria,Number(categoria.id))">
            <label for="nombre" class="form-label">Nombre de la categoría</label>
            <input
                id="nombre"
                type="text"
                v-model="categoria.nombre"
                class="form-input"
                placeholder="Ej: Periféricos"
                required
            />
            <button class="btn primary" type="submit">Guardar Cambios</button>
        </form>
        <router-link class="volver-link" :to="{ name: 'listar_categorias' }">← Volver</router-link>
    </div>
</template>

<style scoped>
.modificar-categoria-container {
    background: #f8fafc;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(79, 140, 255, 0.08);
    padding: 2rem 1.5rem 1.5rem 1.5rem;
    max-width: 400px;
    margin: 2rem auto 0 auto;
    text-align: center;
}

h2 {
    color: #22223b;
    margin-bottom: 1.5rem;
    font-size: 1.4rem;
    font-weight: 600;
}

.modificar-categoria-form {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}

.form-label {
    text-align: left;
    color: #22223b;
    font-weight: 500;
    margin-bottom: 0.2rem;
}

.form-input {
    padding: 0.6rem 0.8rem;
    border: 1px solid #bfc9d9;
    border-radius: 6px;
    font-size: 1rem;
    background: #fff;
    transition: border 0.2s;
}
.form-input:focus {
    border: 1.5px solid #4f8cff;
    outline: none;
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
}
.btn.primary {
    background: #4f8cff;
    color: #fff;
}
.btn.primary:hover,
.btn.primary:focus {
    background: #2563eb;
}

.volver-link {
    display: inline-block;
    margin-top: 1.5rem;
    color: #4f8cff;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}
.volver-link:hover {
    color: #2563eb;
    text-decoration: underline;
}
</style>
