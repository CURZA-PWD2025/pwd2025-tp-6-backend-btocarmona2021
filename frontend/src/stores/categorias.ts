import type { Categoria } from '@/interfaces/categoria'
import { ApiService } from '@/services/ApiServices'
import { defineStore } from 'pinia'
import { ref } from 'vue'

const useCategoriasStore = defineStore('categorias', () => {
    const categorias = ref<Categoria[]>([])
    const categoria = ref<Categoria>({
        id: 0,
        nombre: '',
    })

    async function obtenerTodo() {
        try {
            const data = await ApiService.obtenerTodo('/categorias')
            if (data) {
                categorias.value = data
                return data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function obtenerUno(id: number) {
        try {
            const data = await ApiService.obtenerUno('/categoria', id)
            if (data) {
                categoria.value = data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function crear(categoria: Categoria) {
        try {
            const data = await ApiService.crear('/categoria', categoria)
            if (data) {
                obtenerTodo()
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function modificar(categoria: Categoria, id: number) {
        try {
            const data = await ApiService.modificar('/categoria/', id, categoria)
            if (data) {
                categorias.value = data
            } else {
                console.log(data.error)
            }
        } catch (error: any) {
            
            console.log(error.message)
        }
    }
    async function eliminar(id: number) {
        try {
            const data = await ApiService.eliminar('/categoria/', id)
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
    return { categorias, categoria, obtenerTodo, obtenerUno, crear, modificar, eliminar }
})

export default useCategoriasStore
