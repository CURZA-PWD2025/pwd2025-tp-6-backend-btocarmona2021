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
    <div>
        <router-link :to="{ name: 'crear_marca' }">Crear Marca</router-link>
        <table border="2">
            <caption>
                Listado de Marcas
            </caption>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Descripcion</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(marca, index) in marcas" :key="index">
                    <td>{{ marca.id }}</td>
                    <td>{{ marca.nombre }}</td>
                    <td>
                        <router-link :to="{ name: 'mostrar_marca', params: { id: marca.id } }"
                            ><Icon icon="mdi:show" width="24" height="24"
                        /></router-link>
                        <router-link :to="{ name: 'modificar_marca', params: { id: marca.id } }"
                            ><Icon icon="ic:baseline-mode-edit" width="24" height="24"
                        /></router-link>
                        <button @click.prevent="eliminar(marca.id as number)"><Icon icon="material-symbols:delete" width="24" height="24" style="color: darkred;"/></button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped></style>
