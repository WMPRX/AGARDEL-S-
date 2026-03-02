import { useEffect } from 'react'

export const useWebSocket = (onMessage: (data: any) => void) => {
  useEffect(() => {
    const ws = new WebSocket(import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws')
    ws.onmessage = (ev) => onMessage(JSON.parse(ev.data))
    return () => ws.close()
  }, [onMessage])
}
