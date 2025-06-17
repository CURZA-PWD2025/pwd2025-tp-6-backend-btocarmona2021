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
        try {
            const data = await ApiService.obtenerTodo('/marcas')
            if (data) {
                marcas.value = data
                return data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function obtenerUno(id: number) {
        try {
            const data = await ApiService.obtenerUno('/marca', id)
            if (data) {
                marca.value = data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function crear(marca: Marca) {
        try {
            const data = await ApiService.crear('/marca', marca)
            if (data) {
                obtenerTodo()
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function modificar(marca: Marca, id: number) {
        try {
            const data = await ApiService.modificar('/marca/', id, marca)
            if (data) {
                marcas.value = data
            } else {
                console.log(data.error)
            }
        } catch (error: any) {
            
            console.log(error.message)
        }
    }
    async function eliminar(id: number) {
        try {
            const data = await ApiService.eliminar('/marca/', id)
            if (data) {
                await obtenerTodo()
                console.log(data)
            } else {
                console.log(data.error)
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }
    return { marcas, marca, obtenerTodo, obtenerUno, crear, modificar, eliminar }
})

export default useMarcasStore
