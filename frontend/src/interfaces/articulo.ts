import type { Categoria } from "./categoria"
import type { Marca } from "./marca"
import type { Proveedor } from "./proveedor"

export interface Articulo {
    categorias: Categoria[]
    descripcion: string
    id: number
    marca: Marca
    precio: string
    proveedor: Proveedor
    stock: number
}
