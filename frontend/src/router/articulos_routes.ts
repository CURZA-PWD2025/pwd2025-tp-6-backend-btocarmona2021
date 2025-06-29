export const articulos_routes = [
    {
        path: '/articulos',
        name: 'articulos',
        component: () => import('@/views/ArticulosView.vue'),
        children: [
            {
                path: '',
                name: 'listar_articulos',
                component: () => import('@/components/articulos/ListarArticulos.vue')
            },
            {
                path: ':id/mostrar',
                name: 'mostrar_articulo',
                component: () => import('@/components/articulos/MotrarArticulo.vue'),
            },

            {
                path: 'crear',
                name: 'crear_articulo',
                component: () => import('@/components/articulos/CrearArticulo.vue'),
            },

            {
                path: ':id/modificar',
                name: 'modificar_articulo',
                component: () => import('@/components/articulos/ModificarArticulo.vue'),
            },
        ],
    },
]
