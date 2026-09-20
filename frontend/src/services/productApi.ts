import type { Product } from '../types/product'
import type { Offer } from '../types/offer'

const API_BASE_URL = 'http://127.0.0.1:8000'

export async function fetchProducts(query?: string): Promise<Product[]> {
  const params = new URLSearchParams()

  if (query?.trim()) {
    params.set('q', query.trim())
  }

  const queryString = params.toString()
  const url = queryString
    ? `${API_BASE_URL}/products?${queryString}`
    : `${API_BASE_URL}/products`

  const response = await fetch(url)

  if (!response.ok) {
    throw new Error('Ürünler alınamadı.')
  }

  return response.json() as Promise<Product[]>
}

export async function fetchProductOffers(
  productId: number,
): Promise<Offer[]> {
  const response = await fetch(
    `${API_BASE_URL}/products/${productId}/offers`,
  )

  if (!response.ok) {
    throw new Error('Satıcı teklifleri alınamadı.')
  }

  return response.json() as Promise<Offer[]>
}