import type { Proveedor } from '@/interfaces/proveedor'
import { ApiService } from '@/services/ApiServices'
import { defineStore } from 'pinia'
import { ref } from 'vue'

const useProveedoresStore = defineStore('proveedores', () => {
    const proveedores = ref<Proveedor[]>([])
    const proveedor = ref<Proveedor>({
        direccion: '',
        email: '',
        id: 0,
        nombre: '',
        telefono: '',
    })

    async function obtenerTodo() {
        try {
            const data = await ApiService.obtenerTodo('/proveedores')
            if (data) {
                proveedores.value = data
                return data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function obtenerUno(id: number) {
        try {
            const data = await ApiService.obtenerUno('/proveedor', id)
            if (data) {
                proveedor.value = data
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function crear(proveedor: Proveedor) {
        try {
            const data = await ApiService.crear('/proveedor', proveedor)
            if (data) {
                obtenerTodo()
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }

    async function modificar(proveedor: Proveedor, id: number) {
        try {
            const data = await ApiService.modificar('/proveedor/', id, proveedor)
            if (data) {
                proveedores.value = data
            } else {
                console.log(data.error)
            }
        } catch (error: any) {
            console.log(error.message)
        }
    }
    async function eliminar(id: number) {
        try {
            const data = await ApiService.eliminar('/proveedor/', id)
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
    return { proveedores, proveedor, obtenerTodo, obtenerUno, crear, modificar, eliminar }
})

export default useProveedoresStore
