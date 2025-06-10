import type { Marca } from '@/interfaces/marca'
import { ApiService } from '@/services/ApiServices'
import { defineStore } from 'pinia'
import { ref } from 'vue'

const useMarcasStore = defineStore('marcas', () => {
    const marcas = ref<Marca[]>([])
    const marca = ref<Marca>({
        id: 0,
        nombre: '',
    })

    async function obtenerTodo() {
        const data = await ApiService.obtenerTodo('/marcas')
        if (data) {
            marcas.value = data
            return data
        } else {
            console.log(data.error)
        }
    }
    async function obtenerUno(id: number) {
        const data = await ApiService.obtenerUno('/marca', id)
        if (data) {
            marca.value = data
        } else {
            console.log(data.error)
        }
    }

    async function crear(marca: Marca) { 
        const data = await ApiService.crear('/marca', marca)
        if (data) {
            obtenerTodo()
        } else {
            console.log(data.error)
        }
    }

    async function modificar(marca: Marca, id: number) {
        const data = await ApiService.modificar('/marca/', id, marca)
        if (data) {
            marcas.value = data
        } else {
            console.log(data.error)
        }
    }
    async function eliminar(id: number) {
        const data = await ApiService.eliminar('/marca/', id)
        if (data) {
            await obtenerTodo()
            console.log(data);
            
        } else {
            console.log(data.error)
        }
    }
    return { marcas, marca, obtenerTodo, obtenerUno, crear, modificar, eliminar }
})

export default useMarcasStore
