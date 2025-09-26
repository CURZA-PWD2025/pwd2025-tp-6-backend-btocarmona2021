<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useProveedoresStore from '@/stores/proveedores'
import { useRouter, useRoute } from 'vue-router'

const { proveedor, proveedores } = toRefs(useProveedoresStore())
const { modificar } = useProveedoresStore()
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
    <div class="modificar-proveedor-container">
        <h2>Modificar Proveedor</h2>
        <form
            class="modificar-proveedor-form"
            @submit.prevent="modificar(proveedor, Number(proveedor.id))"
        >
            <label for="nombre" class="form-label">Nombre del proveedor</label>
            <input
                id="nombre"
                type="text"
                v-model="proveedor.nombre"
                class="form-input"
                placeholder="Ej: Tech Solutions SRL"
                required
            />
            <label for="telefono" class="form-label">Teléfono</label>
            <input
                id="telefono"
                type="text"
                v-model="proveedor.telefono"
                class="form-input"
                placeholder="Ej: 1144556677"
                required
            />
            <label for="direccion" class="form-label">Dirección</label>
            <input
                id="direccion"
                type="text"
                v-model="proveedor.direccion"
                class="form-input"
                placeholder="Ej: Av. Córdoba 1234, CABA"
                required
            />
            <label for="email" class="form-label">E-mail</label>
            <input
                id="email"
                type="email"
                v-model="proveedor.email"
                class="form-input"
                placeholder="Ej: contacto@techsolutions.com.ar"
                required
            />
            <button class="btn primary" type="submit">Guardar Cambios</button>
        </form>
        <router-link class="volver-link" :to="{ name: 'listar_proveedores' }">← Volver</router-link>
    </div>
</template>

<style scoped>
.modificar-proveedor-container {
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

.modificar-proveedor-form {
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
