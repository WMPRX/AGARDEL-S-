import { create } from 'zustand'

type State = { running: boolean; mode: string; setStatus: (r: boolean, m: string) => void }
export const useBotStore = create<State>((set) => ({ running: false, mode: 'paper', setStatus: (running, mode) => set({ running, mode }) }))
