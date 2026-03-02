import { useEffect, useState } from 'react'
import axios from 'axios'
export const useTrades = () => {
  const [trades, setTrades] = useState<any[]>([])
  useEffect(() => { axios.get((import.meta.env.VITE_API_URL || 'http://localhost:8000') + '/api/trades').then(r => setTrades(r.data.data)) }, [])
  return trades
}
