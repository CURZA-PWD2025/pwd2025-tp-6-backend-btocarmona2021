<script setup lang="ts">
import { toRefs, watch } from 'vue'
import useCategoriasStore from '@/stores/categorias'
import { useRouter } from 'vue-router'
const { categoria, crear, categorias } = toRefs(useCategoriasStore())

const router = useRouter()

watch(categorias, () => {
    router.push({ name: 'listar_categorias' })
})
</script>

<template>
    <div class="crear-categoria-container">
        <h2>Crear Categoría</h2>
        <form class="crear-categoria-form" @submit.prevent="crear(categoria)">
            <label for="nombre" class="form-label">Nombre de la categoría</label>
            <input
                id="nombre"
                type="text"
                v-model="categoria.nombre"
                class="form-input"
                placeholder="Ej: Periféricos"
                required
            />
            <button class="btn primary" type="submit">Guardar Categoría</button>
        </form>
        <router-link class="volver-link" :to="{ name: 'listar_categorias' }">← Volver</router-link>
    </div>
</template>

<style scoped>
.crear-categoria-container {
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

.crear-categoria-form {
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
    background: #d1fae5; /* verde claro */
    color: #065f46;
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
    background: #22c55e; /* verde principal */
    color: #fff;
}
.btn.primary:hover,
.btn.primary:focus {
    background: #16a34a; /* verde más oscuro al pasar el mouse */
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
