import type { Proveedor } from '@/interfaces/proveedor'
import { ApiService } from '@/services/ApiServices'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useProveedoresStore = defineStore('proveedores', () => {
    const proveedores = ref<Proveedor[]>([])
    const proveedor = ref<Proveedor>({
        id: 0,
        nombre: '',
        direccion: '',
        email: '',
        telefono: '',
    })

    async function obtenerTodo() {
        const data = await ApiService.obtenerTodo('/proveedores')
        if (data) {
            proveedores.value = data
            return data
        } else {
            console.log(data.error)
        }
    }

    async function obtenerUno(id: number) {
        const data = await ApiService.obtenerUno('/proveedor', id)
        if (data) {
            proveedor.value = data
        } else {
            console.log(data.error)
        }
    }

    async function crear(proveedor: Proveedor) {
        const data = await ApiService.crear('/proveedor', proveedor)
        if (data) {
            proveedores.value = data
        } else {
            console.log(data.error)
        }
    }

    async function modificar(proveedor: Proveedor, id: number) {
        const data = await ApiService.modificar('/proveedor/', id, proveedor)
        if (data) {
            proveedores.value = data
        } else {
            console.log(data.error)
        }
    }
    async function eliminar(id: number) {
        const data = await ApiService.eliminar('/proveedor/', id)
        if (data) {
            await obtenerTodo()
        } else {
            console.log(data.error)
        }
    }
    return { proveedores, proveedor, obtenerTodo, obtenerUno, crear, modificar, eliminar }
})

export default useProveedoresStore