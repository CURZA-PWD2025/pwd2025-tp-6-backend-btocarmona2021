export const marcas_routes = [
    {
        path: '/marcas',
        name: 'marcas',
        component: () => import('@/views/MarcasView.vue'),
        children: [
            {
                path: '',
                name: 'listar_marcas',
                component: () => import('@/components/marcas/ListarMarcas.vue'),
            },
            {
                path: ':id/mostrar',
                name: 'mostrar_marca',
                component: () => import('@/components/marcas/MotrarMarca.vue'),
            },

            {
                path: 'crear',
                name: 'crear_marca',
                component: () => import('@/components/marcas/CrearMarca.vue'),
            },

            {
                path: ':id/modificar',
                name: 'modificar_marca',
                component: () => import('@/components/marcas/ModificarMarca.vue'),
            },
        ],
    },
]
