<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useArticulosStore from '@/stores/articulos'
import useMarcasStore from '@/stores/marcas'
import useProveedoresStore from '@/stores/proveedores'
import useCategoriasStore from '@/stores/categorias'
const { articulo, crear, articulos } = toRefs(useArticulosStore())
const { marcas } = toRefs(useMarcasStore())
const { obtenerTodo: obtenerMarcas } = useMarcasStore()
const { proveedores } = toRefs(useProveedoresStore())
const { obtenerTodo: obtenerProveedores } = useProveedoresStore()
const { categorias } = toRefs(useCategoriasStore())
const { obtenerTodo: obtenerCategorias } = useCategoriasStore()

onMounted(async () => {
    articulo.value = {
        id: 0,
        descripcion: 'Ingresar descripción',
        precio: '0',
        stock: 0,
        marca_id: 0,
        marca: { id: 0, nombre: '' },
        proveedor: { id: 0, nombre: '', direccion: '', email: '', telefono: '' },
        proveedor_id: 0,
        categorias: [],
    }
    await obtenerMarcas()
    await obtenerProveedores()
    await obtenerCategorias()
})
</script>

<template>
    <div class="crear-articulo-container">
        <h2>Crear Artículo</h2>
        <form class="crear-articulo-form" @submit.prevent="crear(articulo)">
            <label for="descripcion" class="form-label">Descripción del artículo</label>
            <input
                id="descripcion"
                type="text"
                v-model="articulo.descripcion"
                class="form-input"
                required
            />

            <label for="precio" class="form-label">Precio</label>
            <input
                id="precio"
                type="number"
                v-model="articulo.precio"
                class="form-input"
                required
            />

            <label for="stock" class="form-label">Stock</label>
            <input id="stock" type="number" v-model="articulo.stock" class="form-input" required />

            <label for="marca" class="form-label">Marca</label>
            <select id="marca" v-model="articulo.marca_id" class="form-input" required>
                <option value="" disabled>Seleccione una marca</option>
                <option v-for="marca in marcas" :key="marca.id" :value="marca.id">
                    {{ marca.nombre }}
                </option>
            </select>

            <label for="proveedor" class="form-label">Proveedor</label>
            <select id="proveedor" v-model="articulo.marca_id" class="form-input" required>
                <option value="" disabled>Seleccione un proveedor</option>
                <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor.id">
                    {{ proveedor.nombre }}
                </option>
            </select>
            <label for="categoria" class="form-label">Categorías</label>
            <select
                id="categoria"
                v-model="articulo.categorias"
                class="form-input"
                required
                multiple
            >
                <option value="" disabled>Seleccione una categoría</option>
                <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id">
                    {{ categoria.nombre }}
                </option>
            </select>
            <button class="btn primary" type="submit">Guardar Artículo</button>
        </form>
        <router-link class="volver-link" :to="{ name: 'listar_articulos' }">← Volver</router-link>
    </div>
</template>

<style scoped>
.crear-articulo-container {
    background: #f8fafc;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(79, 140, 255, 0.08);
    padding: 2rem 1.5rem 1.5rem 1.5rem;
    max-width: 500px;
    margin: 2rem auto 0 auto;
    text-align: center;
}

h2 {
    color: #22223b;
    margin-bottom: 1.5rem;
    font-size: 1.4rem;
    font-weight: 600;
}

.crear-articulo-form {
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
