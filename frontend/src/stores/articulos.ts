import type { Articulo } from '@/interfaces/articulo'
import { ApiService } from '@/services/ApiServices'
import { defineStore } from 'pinia'
import { ref } from 'vue'

const useArticulosStore = defineStore('articulos', () => {
    const articulos = ref<Articulo[]>([])
    const articulo = ref<Articulo>({
        categorias: [],
        descripcion: '',
        id: 0,
        marca: { id: 0, nombre: '' },
        precio: '',
        proveedor: {
            direccion: '',
            email: '',
            id: 0,
            nombre: '',
            telefono: '',
        },
        stock: 0,
    })

    async function obtenerTodo() {
        try {
            const data = await ApiService.obtenerTodo('/articulos')
            if (data) {
                articulos.value = data
                return data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function obtenerUno(id: number) {
        try {
            const data = await ApiService.obtenerUno('/articulo', id)
            if (data) {
                articulo.value = data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function crear(articulo: Articulo) {
        
        try {
            const data = await ApiService.crear('/articulo', articulo)
            if (data) {
                obtenerTodo()
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function modificar(articulo: Articulo, id: number) {
        try {
            const data = await ApiService.modificar('/articulo/', id, articulo)
            if (data) {
                articulos.value = data
            } else {
                console.log(data.error)
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }
    async function eliminar(id: number) {
        try {
            const data = await ApiService.eliminar('/articulo/', id)
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
    return { articulos, articulo, obtenerTodo, obtenerUno, crear, modificar, eliminar }
})

export default useArticulosStore
