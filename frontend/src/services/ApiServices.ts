import type { Marca } from '@/interfaces/marca'
import { api } from '@/plugins/axios'

export class ApiService {
    static async obtenerTodo(url: string) {
        try {
            const respuesta = await api.get(url) 
            if (respuesta.status === 200) {
                return respuesta.data
            } else {
                return respuesta.data.error
            }
        } catch (error:any) {
            return error.message
        }
    }
    static async obtenerUno(url: string, id: number) {
        try {
            const respuesta = await api.get(url + id)
            if (respuesta) {
                return respuesta.data
            }
        } catch (error:any) {
            return error.message
        }
    }
    static async crear(url: string, data: object) {
        console.log(data);
        
        try {
            const respuesta = await api.post(url, data)
            if (respuesta) {
                return respuesta.data
            }
        } catch (error:any) {
            return error.message
        }
    }
    static async modificar(url: string, id: number, marca: Object) {
        try {
            const respuesta = await api.put(url + id, marca)
            if (respuesta) {
                return respuesta.data
            }
        } catch (error:any) {
            return error.message
        }
    }
    static async eliminar(url: string, id: number) {
        try {
            const respuesta = await api.delete(url + id)
            return respuesta.data
        } catch (error:any) {
            return error.message
        }
    }
}
