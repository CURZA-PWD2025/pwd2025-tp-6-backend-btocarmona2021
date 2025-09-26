<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useMarcasStore from '@/stores/marcas'
import { useRouter, useRoute } from 'vue-router'

const { marca, marcas } = toRefs(useMarcasStore())
const { modificar } = useMarcasStore()
const router = useRouter()
const route = useRoute()

watch(marcas, () => {
    router.push({ name: 'listar_marcas' })
})

onMounted(() => {
    const id = Number(route.params.id)
    marca.value = marcas.value.find((marca) => marca.id === id) || { id: 0, nombre: '' }
})
</script>

<template>
    <div class="modificar-marca-container">
        <h2>Modificar Marca</h2>
        <form class="modificar-marca-form" @submit.prevent="modificar(marca,Number(marca.id))">
            <label for="nombre" class="form-label">Nombre de la marca</label>
            <input
                id="nombre"
                type="text"
                v-model="marca.nombre"
                class="form-input"
                placeholder="Ej: Lenovo"
                required
            />
            <button class="btn primary" type="submit">Guardar Cambios</button>
        </form>
        <router-link class="volver-link" :to="{ name: 'listar_marcas' }">← Volver</router-link>
    </div>
</template>

<style scoped>
.modificar-marca-container {
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

.modificar-marca-form {
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
