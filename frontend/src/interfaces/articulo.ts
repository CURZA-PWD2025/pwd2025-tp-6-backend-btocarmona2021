export interface Articulo {
    categorias:  Categorias;
    descripcion: string;
    id:          number;
    marca:       Categorias;
    precio:      string;
    proveedor:   Proveedor;
    stock:       number;
}

export interface Categorias {
    id:     number;
    nombre: string;
}

export interface Proveedor {
    direccion: string;
    email:     string;
    id:        number;
    nombre:    string;
    telefono:  string;
}
