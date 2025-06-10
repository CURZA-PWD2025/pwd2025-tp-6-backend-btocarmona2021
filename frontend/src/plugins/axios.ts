import axios from 'axios'

export const api = axios.create({
    baseURL: 'http://168.196.24.141:5000/api/v1/',
    timeout: 1000,
})
