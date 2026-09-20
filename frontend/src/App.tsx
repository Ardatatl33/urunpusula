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
    <main className="product-page">
      <h1>ÜrünPusula</h1>

      {isLoading && <p className="status-message">Ürünler yükleniyor...</p>}
      {error && <p className="status-message error-message">{error}</p>}

      {!isLoading && !error && (
        <ul className="product-list">
          {products.map((product) => (
            <li className="product-card" key={product.id}>
              <h2>
                {product.brand} {product.name}
              </h2>
              <p className="product-specs">
                {product.storage_gb} GB depolama · {product.ram_gb} GB RAM
              </p>
              <p className="product-specs">
                {product.screen_inches} inç ekran · {product.battery_mah} mAh pil
              </p>
              <p className="product-specs">
                {product.main_camera_mp} MP ana kamera ·{' '}
                {product.has_5g ? '5G destekli' : '5G desteği yok'}
              </p>
            </li>
          ))}
        </ul>
      )}
    </main>
  )
}

export default App
