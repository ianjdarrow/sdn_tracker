import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
// import Individuals from '@/components/Individuals'
// import Entities from '@/components/Entities'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    // {
    //   path: '/individuals',
    //   name: 'Individuals',
    //   component: Individuals
    // },
    // {
    //   path: '/entities',
    //   name: 'Entities',
    //   component: Entities
    // }
  ]
})
