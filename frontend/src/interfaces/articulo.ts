import type { Categoria } from "./categoria"
import type { Marca } from "./marca"
import type { Proveedor } from "./proveedor"

export interface Articulo {
    categorias: Categoria[]
    descripcion: string
    id?: number
    marca: Marca
    marca_id?:number
    precio: string
    proveedor: Proveedor
    proveedor_id?:number
    stock: number
}
