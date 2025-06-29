export const categorias_routes = [
    {
        path: '/categorias',
        name: 'categorias',
        component: () => import('@/views/CategoriasView.vue'),
        children: [
            {
                path: '',
                name: 'listar_categorias',
                component: () => import('@/components/categorias/ListarCategorias.vue')
            },
            {
                path: ':id/mostrar',
                name: 'mostrar_categoria',
                component: () => import('@/components/categorias/MotrarCategoria.vue'),
            },

            {
                path: 'crear',
                name: 'crear_categoria',
                component: () => import('@/components/categorias/CrearCategoria.vue'),
            },

            {
                path: ':id/modificar',
                name: 'modificar_categoria',
                component: () => import('@/components/categorias/ModificarCategoria.vue'),
            },
        ],
    },
]
