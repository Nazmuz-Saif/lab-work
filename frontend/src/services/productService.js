import api from "./api.js";

export const listProducts = () => api.get("/products/").then((r) => r.data);

export const createProduct = (payload) => api.post("/products/", payload).then((r) => r.data);
