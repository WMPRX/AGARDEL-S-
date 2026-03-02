import { useEffect } from 'react'
import axios from 'axios'
import { useBotStore } from '../store/botStore'

export const useBotState = () => {
  const setStatus = useBotStore((s) => s.setStatus)
  useEffect(() => {
    const t = setInterval(async () => {
      const res = await axios.get((import.meta.env.VITE_API_URL || 'http://localhost:8000') + '/api/bot/status')
      setStatus(res.data.data.running, res.data.data.mode)
    }, 3000)
    return () => clearInterval(t)
  }, [setStatus])
}
