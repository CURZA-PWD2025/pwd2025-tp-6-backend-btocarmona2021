export const proveedores_routes = [
    {
        path: '/proveedores',
        name: 'proveedores',
        component: () => import('@/views/ProveedorView.vue'),
        children: [
            {
                path: '',
                name: 'listar_proveedores',
                component: () => import('@/components/proveedores/ListarProveedores.vue')
            },
            {
                path: ':id/mostrar',
                name: 'mostrar_proveedor',
                component: () => import('@/components/proveedores/MotrarProveedor.vue'),
            },

            {
                path: 'crear',
                name: 'crear_proveedor',
                component: () => import('@/components/proveedores/CrearProveedor.vue'),
            },

            {
                path: ':id/modificar',
                name: 'modificar_proveedor',
                component: () => import('@/components/proveedores/ModificarProveedor.vue'),
            },
        ],
    },
]
