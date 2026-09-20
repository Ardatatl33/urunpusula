import { useEffect, useState, type FormEvent } from 'react'
import './App.css'
import { fetchProductOffers, fetchProducts } from './services/productApi'
import type { Product } from './types/product'
import type { Offer } from './types/offer'

function App() {
  const [products, setProducts] = useState<Product[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')
  const [searchText, setSearchText] = useState('')
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedProductId, setSelectedProductId] = useState<number | null>(null)
  const [offers, setOffers] = useState<Offer[]>([])
  const [isOffersLoading, setIsOffersLoading] = useState(false)
  const [offersError, setOffersError] = useState('')

  useEffect(() => {
    setIsLoading(true)
    setError('')

    fetchProducts(searchQuery)
      .then(setProducts)
      .catch(() => setError('Ürünler yüklenemedi.'))
      .finally(() => setIsLoading(false))
  }, [searchQuery])

  function handleSearch(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setSearchQuery(searchText)
  }

  async function handleShowOffers(productId: number) {
    setSelectedProductId(productId)
    setIsOffersLoading(true)
    setOffersError('')

    try {
      const productOffers = await fetchProductOffers(productId)
      setOffers(productOffers)
    } catch {
      setOffersError('Satıcı teklifleri yüklenemedi.')
      setOffers([])
    } finally {
      setIsOffersLoading(false)
    }
  }

  return (
    <main className="product-page">
      <h1>ÜrünPusula</h1>

      <form onSubmit={handleSearch}>
        <input
          type="search"
          value={searchText}
          onChange={(event) => setSearchText(event.target.value)}
          placeholder="Telefon ara..."
        />
        <button type="submit">Ara</button>
      </form>

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

              <button
                type="button"
                onClick={() => handleShowOffers(product.id)}
              >
                Teklifleri göster
              </button>

              {selectedProductId === product.id && (
                <section className="offer-section">
                  <h3>Satıcı teklifleri</h3>

                  {isOffersLoading && <p>Teklifler yükleniyor...</p>}
                  {offersError && <p className="error-message">{offersError}</p>}

                  {!isOffersLoading && !offersError && (
                    <ul className="offer-list">
                      {offers.map((offer) => (
                        <li key={offer.id}>
                          <span>
                            {offer.marketplace} · {offer.seller_name}
                          </span>
                          <strong>
                            {Number(offer.price).toLocaleString('tr-TR')} TL
                          </strong>
                          <span>Satıcı puanı: {offer.seller_rating}</span>
                          <a href={offer.url} target="_blank" rel="noreferrer">
                            Teklife git
                          </a>
                        </li>
                      ))}
                    </ul>
                  )}
                </section>
              )}
            </li>
          ))}
        </ul>
      )}
    </main>
  )
}

export default App
