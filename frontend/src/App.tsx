import { useEffect, useState } from 'react'
import './App.css'
import { fetchProducts } from './services/productApi'
import type { Product } from './types/product'

function App() {
  const [products, setProducts] = useState<Product[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchProducts()
      .then(setProducts)
      .catch(() => setError('Ürünler yüklenemedi.'))
      .finally(() => setIsLoading(false))
  }, [])

  return (
    <main>
      <h1>ÜrünPusula</h1>

      {isLoading && <p>Ürünler yükleniyor...</p>}
      {error && <p>{error}</p>}

      {!isLoading && !error && (
        <ul>
          {products.map((product) => (
            <li key={product.id}>
              <strong>
                {product.brand} {product.name}
              </strong>
              <span>
                {product.storage_gb} GB · {product.ram_gb} GB RAM ·{' '}
                {product.screen_inches} inç
              </span>
            </li>
          ))}
        </ul>
      )}
    </main>
  )
}

export default App