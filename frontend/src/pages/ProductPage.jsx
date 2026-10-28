import { useEffect, useState } from "react";
import axios from "axios";

const API = "http://localhost:8000/api/v1/products/";

export default function ProductPage() {
  const [form, setForm] = useState({ product_code: "", product_name: "", price: "" });
  const [products, setProducts] = useState([]);
  const [error, setError] = useState("");

  const loadProducts = () => {
    axios.get(API).then((res) => setProducts(res.data));
  };

  useEffect(loadProducts, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post(API, form)
      .then(() => {
        setForm({ product_code: "", product_name: "", price: "" });
        setError("");
        loadProducts();
      })
      .catch((err) => {
        const errors = Object.entries(err.response.data);
        setError(errors.map(([field, message]) => field + ": " + message).join(", "));
      });
  };

  return (
    <div className="mx-auto max-w-xl p-6">
      <h1 className="text-2xl font-bold">Products</h1>

      <form onSubmit={handleSubmit} className="mt-4 space-y-2">
        <input id="product_code" name="product_code" placeholder="Product code" value={form.product_code} onChange={handleChange} className="w-full border p-2" />
        <input id="product_name" name="product_name" placeholder="Product name" value={form.product_name} onChange={handleChange} className="w-full border p-2" />
        <input id="price" name="price" placeholder="Price" value={form.price} onChange={handleChange} className="w-full border p-2" />
        <button id="save" type="submit" className="bg-blue-600 px-4 py-2 text-white">Save</button>
      </form>

      {error && <p id="error" className="mt-2 text-red-600">{error}</p>}

      <table id="list" className="mt-6 w-full text-left">
        <thead>
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.product_code}>
              <td>{p.product_code}</td>
              <td>{p.product_name}</td>
              <td>{p.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
