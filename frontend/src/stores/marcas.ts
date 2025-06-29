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
    const errores = ref('')

    async function obtenerTodo() {
        try {
            const data = await ApiService.obtenerTodo('/marcas')
            if (data) {
                marcas.value = data
            }
        } catch (error: any) {
            errores.value = error.message
        }
    }

    async function obtenerUno(id: number) {
        try {
            const data = await ApiService.obtenerUno('/marca', id)
            if (data) {
                marca.value = data
                return data
            }
        } catch (error: any) {
            errores.value = error.message
        }
    }

    async function crear(marca: Marca) {
        try {
            if (!marca.nombre) {
                throw new Error('Debe completar el campo nombre')
            }
            const data = await ApiService.crear('/marca', marca)
            if (data) {
                obtenerTodo()
                errores.value = ''
            }
        } catch (error: any) {
            errores.value = error.message
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
            errores.value = error.message
        }
    }
    async function eliminar(id: number) {
        try {
            const data = await ApiService.eliminar('/marca/', id)
            if (data) {
                await obtenerTodo()
            }
        } catch (error: any) {
            errores.value = error.message
        }
    }
    return { marcas, marca, errores, obtenerTodo, obtenerUno, crear, modificar, eliminar }
})

export default useMarcasStore
